"""
Gera as páginas de Oficinas a partir de um molde só.

Pra adicionar ou mudar uma oficina:
1. Mexa na lista OFICINAS lá embaixo.
2. Rode:  python3 ferramentas/gerar.py
3. Salve no GitHub.

Topo e rodapé ficam aqui também. Se mudar o menu, mude aqui E no index.html da Home.

Também faz, a cada rodada:
- prepara as fotos novas de fotos-originais/ (ver imagens.py);
- preenche os trechos marcados da Home (<!-- gerado:... -->);
- a página de erro (404.html) e o mapa do site pro Google (sitemap.xml).
"""
import re
from pathlib import Path
from html import escape
from urllib.parse import quote

from imagens import foto, existe, preparar_fotos, registrar_oficinas

RAIZ = Path(__file__).resolve().parent.parent
WHATS = "5551989201232"

# Endereço do site no ar. Se um dia tiver domínio próprio, troque só aqui
# (e BASE vira "/").
SITE = "https://camilaraposaarte.github.io/site-camila-raposa/"
BASE = "/site-camila-raposa/"


def whats(texto):
    return f"https://wa.me/{WHATS}?text={quote(texto)}"


def cabeca_meta(r, titulo_completo, descricao, caminho):
    """Título, descrição, prévia do WhatsApp/redes e ícone da aba."""
    url = SITE + caminho
    imagem = ""
    if existe("compartilhar"):
        imagem = f"""
  <meta property="og:image" content="{SITE}assets/img/compartilhar.jpg">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">"""
    return f"""<title>{escape(titulo_completo)}</title>
  <meta name="description" content="{escape(descricao)}">
  <link rel="canonical" href="{url}">
  <meta property="og:type" content="website">
  <meta property="og:locale" content="pt_BR">
  <meta property="og:site_name" content="Camila Raposa">
  <meta property="og:title" content="{escape(titulo_completo)}">
  <meta property="og:description" content="{escape(descricao)}">
  <meta property="og:url" content="{url}">{imagem}
  <meta name="twitter:card" content="{'summary_large_image' if imagem else 'summary'}">
  <link rel="icon" href="{r}assets/img/favicon.svg" type="image/svg+xml">
  <meta name="theme-color" content="#1B5B7E">"""


def marca(r):
    """Nome no topo. Quando o logo chegar, ele aparece antes do nome."""
    logo = ""
    if existe("logo"):
        logo = f'<img class="marca-logo" src="{r}assets/img/logo-800.webp" alt="" width="48" height="48">'
    return f'<a class="marca" href="{r or "./"}">{logo}Camila Raposa{"" if logo else " 🦊"}</a>'


def topo(r, titulo, descricao, atual="", caminho=None):
    if caminho is None:
        caminho = f"{atual}/" if atual else ""
    def item(href, nome, extra=""):
        cur = ' aria-current="page"' if atual == href else ""
        return f'<li><a{extra} href="{r}{href}/"{cur}>{nome}</a></li>'

    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  {cabeca_meta(r, f"{titulo} · Camila Raposa", descricao, caminho)}
  <link rel="preload" href="{r}assets/fonts/caprasimo.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="{r}assets/fonts/comfortaa-400.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="{r}assets/css/estilo.css">
</head>
<body>
  <a class="pular" href="#conteudo">Pular para o conteúdo</a>

  <header class="topo">
    <div class="miolo">
      {marca(r)}
      <button class="botao-menu" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
      <nav class="menu" id="menu" aria-label="Menu principal">
        <ul>
          {item("aulas", "Aulas")}
          {item("oficinas", "Oficinas")}
          {item("portfolio", "Portfólio")}
          {item("sobre", "Sobre")}
          {item("contato", "Contato", ' class="menu-contato"')}
        </ul>
      </nav>
    </div>
  </header>

  <main id="conteudo">
"""


def rodape(r):
    return f"""  </main>

  <footer class="rodape">
    <div class="miolo">
      <div>
        <h2>Fale comigo</h2>
        <ul>
          <li>WhatsApp: <a href="https://wa.me/{WHATS}">(51) 98920-1232</a></li>
          <li>Aulas presenciais: Koralle, Av. José Bonifácio, 95, Farroupilha, Porto Alegre</li>
        </ul>
      </div>
      <div>
        <h2>No site</h2>
        <ul>
          <li><a href="{r}eventos/">Eventos</a></li>
          <li><a href="{r}materiais/">Lista de materiais</a></li>
          <li><a href="{r}psicopedagogia/">Psicopedagogia</a></li>
        </ul>
      </div>
      <div>
        <h2>Nas redes</h2>
        <ul>
          <li><a href="https://www.instagram.com/camilaraposa/">Instagram</a></li>
          <li><a href="https://www.youtube.com/@CamilaRaposa">YouTube</a></li>
          <li><a href="https://www.tiktok.com/@camilaraposa">TikTok</a></li>
          <li><a href="https://www.behance.net/camilaraposaarte">Behance</a></li>
          <li><a href="https://br.pinterest.com/camilaraposaref/">Pinterest</a></li>
          <li><a href="https://www.linkedin.com/in/camilaraposa/">LinkedIn</a></li>
        </ul>
      </div>
      <p class="final">Arte é para todos. Prof. Camila Raposa 🦊</p>
    </div>

    <!-- botão fixo no canto; fica dentro do rodapé pra leitor de tela achar -->
    <a class="whats-flutuante" href="https://wa.me/{WHATS}" aria-label="Chamar a Camila no WhatsApp">
      <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M12 3a9 9 0 0 0-7.8 13.5L3 21l4.6-1.2A9 9 0 1 0 12 3Z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></svg>
      <span>WhatsApp</span>
    </a>
  </footer>


  <script src="{r}assets/js/menu.js"></script>
</body>
</html>
"""


# ---------------------------------------------------------------
# AS OFICINAS
# Campos: slug, nome, frase (aparece no cartão), descricao,
#         explora (lista), recebe (lista), kit (lista, pode ser vazia),
#         idade, material
# Ordem da lista = ordem no site.
# ---------------------------------------------------------------

KIT_AQUARELA = [
    "1 kit de amostras de aquarela Pentel, cores variadas",
    "5 papéis de aquarela sortidos",
    "1 pincel redondo tipo bulbo",
    "1 adesivo exclusivo Camila Raposa",
    "1 totebag exclusiva Camila Raposa",
    "1 apostila com o conteúdo da oficina",
]
RECEBE_PADRAO = [
    "Coffee break (me avise se tiver alguma alergia)",
    "Kit iniciante pra continuar praticando em casa",
    "Brindes dos nossos parceiros",
]

OFICINAS = [
    dict(
        slug="aquarela-iniciantes",
        nome="Aquarela para iniciantes",
        frase="Água, cor e transparência, do primeiro pincel.",
        descricao=[
            "Os fundamentos da aquarela de um jeito leve, divertido e sem julgamento.",
            "É pra quem nunca pintou ou pra quem só quer se dar a chance de criar. Aqui, cada pincelada é uma descoberta.",
        ],
        explora=[
            "Técnicas básicas de pintura com aquarela",
            "Controle da água e transparência das cores",
            "Efeitos simples que dão vida ao que você cria",
        ],
        recebe=RECEBE_PADRAO,
        kit=KIT_AQUARELA,
        idade="A partir de 8 anos",
        material="Incluso. Você testa aquarelas, pincéis e papéis diferentes.",
    ),
    dict(
        slug="aquarela-flores-frutas",
        nome="Aquarela flores e frutas",
        frase="Pintar a natureza com técnicas simples.",
        descricao=[
            "Um mergulho nas cores e formas da natureza: flores delicadas e frutas bem vivas.",
            "Serve pra quem está começando e pra quem quer praticar com temas leves.",
        ],
        explora=[
            "Técnicas básicas de aquarela",
            "Mistura de cores e transparências",
            "Composição simples com flores e frutas",
        ],
        recebe=RECEBE_PADRAO,
        kit=KIT_AQUARELA,
        idade="A partir de 8 anos",
        material="Incluso. Você testa aquarelas e papéis diferentes.",
    ),
    dict(
        slug="gatitos-aquarela",
        nome="Gatitos e aquarela",
        frase="Você pinta um gatinho e leva pra casa.",
        descricao=[
            "Técnicas básicas de aquarela com um objetivo bem gostoso: no fim do encontro, você tem um gatinho pintado por você pra levar pra casa.",
        ],
        explora=[
            "Técnicas básicas de aquarela",
            "Controle da água e da cor",
            "Um gatinho do primeiro traço até a última pincelada",
        ],
        recebe=[
            "Coffee break (me avise se tiver alguma alergia)",
            "Kit pra continuar praticando em casa",
        ],
        kit=[],
        idade="A partir de 8 anos",
        material="Incluso.",
    ),
    dict(
        slug="aquarela-natal",
        nome="Aquarela de Natal",
        frase="Cartões e enfeites pintados à mão.",
        descricao=[
            "A magia do Natal em aquarela: cartões, ilustrações e lembrancinhas feitas com afeto.",
            "Não precisa saber pintar. Todo mundo é bem-vindo.",
        ],
        explora=[
            "Técnicas básicas de aquarela com temas de Natal",
            "Guirlandas, pinheiros, luzes e doces",
            "Composição pra cartões e artes decorativas",
        ],
        recebe=[
            "Coffee break com gostinho de Natal (me avise se tiver alguma alergia)",
            "Kit iniciante pra continuar criando em casa",
            "Brindes natalinos dos nossos parceiros",
        ],
        kit=KIT_AQUARELA,
        idade="A partir de 8 anos",
        material="Incluso. Aquarelas, pincéis e papéis pra experimentar.",
    ),
    dict(
        slug="aquarela-halloween",
        nome="Aquarela de Halloween",
        frase="Fantasmas fofos, abóboras e caldeirões.",
        descricao=[
            "O lado mais divertido do Dia das Bruxas, em aquarela.",
            "Fantasmas fofinhos, abóboras sorridentes e poções encantadas, pra quem quer se aventurar sem medo.",
        ],
        explora=[
            "Técnicas básicas de aquarela com temas de Halloween",
            "Mistura de cores sombrias e vibrantes",
            "Chapéus, gatos pretos, doces e caldeirões",
        ],
        recebe=[
            "Coffee break com gostinho de outono (me avise se tiver alguma alergia)",
            "Kit iniciante pra praticar em casa",
            "Brindes temáticos dos nossos parceiros",
        ],
        kit=KIT_AQUARELA,
        idade="A partir de 8 anos",
        material="Incluso. Aquarelas, pincéis e papéis variados.",
    ),
    dict(
        slug="lapis-aquarelavel",
        nome="Lápis de cor aquarelável",
        frase="O lápis que vira tinta com água.",
        descricao=[
            "Um material versátil que junta o melhor do desenho e da pintura.",
            "Tudo de um jeito descomplicado, prático e divertido.",
        ],
        explora=[
            "Técnicas básicas de ativação com água",
            "Misturas e efeitos em papéis diferentes",
            "Truques pra colorir com mais leveza e controle",
        ],
        recebe=RECEBE_PADRAO,
        kit=[
            "3 lápis aquareláveis de alta qualidade, cores sortidas",
            "5 papéis de aquarela 300 g, marcas sortidas",
            "1 pincel com reservatório",
            "1 adesivo exclusivo Camila Raposa",
            "1 totebag exclusiva Camila Raposa",
            "1 apostila com o conteúdo da oficina",
        ],
        idade="A partir de 8 anos",
        material="Incluso. Você testa vários lápis aquareláveis e pincéis.",
    ),
    dict(
        slug="marcadores-alcool",
        nome="Marcadores a álcool",
        frase="Degradê e sombra sem manchar.",
        descricao=[
            "As bases pra usar esse material vibrante, cheio de possibilidades.",
            "Bom pra quem quer ilustrar, colorir livros ou dar vida às próprias criações.",
        ],
        explora=[
            "Técnicas básicas de aplicação e sombreamento",
            "Mistura de cores e degradês suaves",
            "Como controlar o fluxo e evitar manchas",
        ],
        recebe=RECEBE_PADRAO,
        kit=[
            "3 marcadores a álcool, cores sortidas",
            "5 artes em papel bristol pra praticar",
            "1 adesivo exclusivo Camila Raposa",
            "1 totebag exclusiva Camila Raposa",
            "1 apostila com o conteúdo da oficina",
        ],
        idade="A partir de 8 anos",
        material="Incluso. Você testa vários marcadores profissionais.",
    ),
    dict(
        slug="lettering",
        nome="Lettering sem julgamentos",
        frase="Desenhar letras sem medo da letra feia.",
        descricao=[
            "A arte de desenhar letras de forma livre, sem a pressão da perfeição.",
            "É pra soltar a mão e brincar com formas, mesmo que você ache sua letra feia. Spoiler: ela não é.",
        ],
        explora=[
            "Fundamentos do lettering e tipos de traço",
            "Combinações de palavras, formas e emoções",
            "Exercícios pra soltar o traço e criar com identidade",
        ],
        recebe=RECEBE_PADRAO,
        kit=[
            "3 canetas brush grandes",
            "3 canetas brush pequenas",
            "Folhas pontilhadas pra praticar",
            "1 adesivo exclusivo Camila Raposa",
            "1 totebag exclusiva Camila Raposa",
            "1 apostila com o conteúdo da oficina",
        ],
        idade="A partir de 8 anos",
        material="Incluso. Canetas, brush pens e papéis pra explorar.",
    ),
    dict(
        slug="horror-de-pintar",
        nome="Horror de pintar",
        frase="Nanquim, sombra e monstros na mancha.",
        descricao=[
            "Criaturas e cenas assustadoras com nanquim preto, mesmo pra quem está começando.",
            "Traço, contraste e sombra até o papel ficar bem sinistro. Você sai com as suas próprias ilustrações de terror.",
        ],
        explora=[
            "Olhos e dentes: o que deixa um rosto incômodo",
            "Alto contraste: quando o normal vira assustador",
            "Achar o monstro na mancha, direto no nanquim",
        ],
        recebe=[
            "Coffee break",
            "Todo o material pra usar na oficina",
        ],
        kit=[],
        idade="A partir de 12 anos",
        material="Incluso. Não precisa levar nada.",
    ),
    dict(
        slug="gambiarra-artistica",
        nome="Gambiarra artística",
        frase="Café, papelão e o que mais pintar.",
        descricao=[
            "Aqui a regra é simples: se dá pra criar, vale.",
            "Materiais inusitados, reaproveitados e até esquecidos, como café, vinho e papelão. E ainda: consertar pincel, ressuscitar tinta seca e transformar erro em efeito.",
        ],
        explora=[
            "Técnicas com materiais alternativos: café, vinho, carvão, papel craft",
            "Como recuperar e reaproveitar material de arte",
            "Exercícios de improviso e liberdade",
        ],
        recebe=[
            "Coffee break com cara de ateliê (me avise se tiver alguma alergia)",
            "Kit criativo com itens reaproveitados e surpresas",
            "Brindes dos nossos parceiros",
        ],
        kit=[
            "1 adesivo exclusivo Camila Raposa",
            "1 totebag exclusiva Camila Raposa",
            "1 apostila com o conteúdo da oficina",
        ],
        idade="A partir de 8 anos",
        material="Incluso. Se quiser, traga seus cacarecos artísticos.",
    ),
]


def lista(itens):
    return "\n".join(f"            <li>{escape(i)}</li>" for i in itens)


def cartoes(r):
    linhas = []
    for o in OFICINAS:
        linhas.append(
            f'          <li><a href="{r}oficinas/{o["slug"]}/">'
            + foto(f"oficina-{o['slug']}", r, "Foto da oficina", forma="quadrada", tag="span") +
            f'<span class="cartao-nome">{escape(o["nome"])}</span>'
            f'<span class="cartao-desc">{escape(o["frase"])}</span></a></li>'
        )
    return "\n".join(linhas)


def pagina_oficina(o):
    r = "../../"
    pedido = whats(f"Oi, Camila! Quero saber da próxima turma da oficina {o['nome']}.")
    fatos = []
    if o["idade"]:
        fatos.append(("Idade", o["idade"]))
    if o["material"]:
        fatos.append(("Material", o["material"]))
    fatos_html = "\n".join(
        f'            <div><dt>{escape(k)}</dt><dd>{escape(v)}</dd></div>' for k, v in fatos
    )
    desc = "\n".join(f"          <p>{escape(p)}</p>" for p in o["descricao"])

    recebe = ""
    if o["recebe"]:
        recebe = f"""
          <h2 class="titulo-bloco">O que você recebe</h2>
          <ul class="lista-marcada">
{lista(o["recebe"])}
          </ul>"""

    kit = ""
    if o["kit"]:
        kit = f"""
          <div class="caixa">
            <h2 class="titulo-bloco">O que vem no kit</h2>
            <ul class="lista-marcada">
{lista(o["kit"])}
            </ul>
          </div>"""

    outras = "\n".join(
        f'          <li><a href="../{x["slug"]}/">{escape(x["nome"])}</a></li>'
        for x in OFICINAS if x["slug"] != o["slug"]
    )

    corpo = f"""
    <section class="pagina-topo">
      <div class="miolo">
        <p class="caminho"><a href="../">Oficinas</a></p>
        <h1>{escape(o["nome"])}</h1>
        <p class="pagina-frase">{escape(o["frase"])}</p>
        <a class="botao botao--whats" href="{pedido}">Quero participar</a>
      </div>
    </section>

    <section class="secao">
      <div class="miolo colunas">
        <div>
{desc}
          <h2 class="titulo-bloco">Você vai explorar</h2>
          <ul class="lista-marcada">
{lista(o["explora"])}
          </ul>{recebe}
          <dl class="fatos">
{fatos_html}
          </dl>
        </div>
        <div>
          {foto(f"oficina-{o['slug']}", r, "Foto da oficina")}{kit}
        </div>
      </div>
    </section>

    <section class="secao secao--rosa">
      <div class="miolo">
        <h2>Próxima turma</h2>
        <p>As datas novas saem no Instagram e no WhatsApp. Quer saber quando abrir? Me chama.</p>
        <a class="botao botao--whats" href="{pedido}">Quero saber da próxima turma</a>
      </div>
    </section>

    <section class="secao">
      <div class="miolo">
        <h2>Outras oficinas</h2>
        <ul class="outras">
{outras}
        </ul>
      </div>
    </section>
"""
    descricao_meta = f"Oficina {o['nome']} com a Camila Raposa, em Porto Alegre. {o['frase']}"
    return topo(r, o["nome"], descricao_meta, "oficinas", f"oficinas/{o['slug']}/") + corpo + rodape(r)


def pagina_indice_oficinas():
    r = "../"
    corpo = f"""
    <section class="pagina-topo">
      <div class="miolo">
        <h1>Oficinas</h1>
        <p class="pagina-frase">Um encontro, um tema, todo o material na mesa. Ninguém precisa saber desenhar.</p>
      </div>
    </section>

    <section class="secao">
      <div class="miolo">
        <ul class="cartoes">
{cartoes(r)}
        </ul>
      </div>
    </section>

    <section class="secao secao--rosa">
      <div class="miolo">
        <h2>Oficina pra sua festa ou empresa</h2>
        <p>Qualquer oficina pode virar uma festa de aniversário, um encontro de equipe ou uma atividade no seu evento.</p>
        <a class="botao botao--petroleo" href="../eventos/">Ver eventos</a>
      </div>
    </section>
"""
    return topo(r, "Oficinas", "Oficinas de aquarela, lettering, marcadores, nanquim e mais com a Camila Raposa, em Porto Alegre.", "oficinas") + corpo + rodape(r)


def pagina_404():
    """Página de endereço errado. O GitHub mostra ela em qualquer pasta,
    então os links usam o caminho completo (BASE) em vez de ../"""
    r = BASE
    corpo = f"""
    <section class="pagina-topo">
      <div class="miolo">
        <h1>Essa página não existe</h1>
        <p class="pagina-frase">Pode ser um endereço digitado errado, ou uma página que mudou de lugar.</p>
        <div class="acoes">
          <a class="botao botao--rosa" href="{r}">Ir pro começo do site</a>
          <a class="botao botao--contorno" href="{r}oficinas/">Ver as oficinas</a>
        </div>
      </div>
    </section>

    <section class="secao">
      <div class="miolo">
        <h2>Procurando alguma coisa?</h2>
        <p>Me chama no WhatsApp que eu te ajudo a achar.</p>
        <a class="botao botao--whats" href="{whats("Oi, Camila! Tentei abrir uma página do teu site e não achei.")}">Chamar no WhatsApp</a>
      </div>
    </section>
"""
    html = topo(r, "Página não encontrada", "Essa página não existe no site da Camila Raposa.", caminho="404.html")
    html = html.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n  <meta name="robots" content="noindex">')
    return html + corpo + rodape(r)


def sitemap():
    """Lista de todas as páginas, pro Google achar o site inteiro."""
    paginas = sorted(
        p.parent.relative_to(RAIZ).as_posix()
        for p in RAIZ.glob("**/index.html")
        if not any(parte.startswith(".") or parte in ("prints", "fotos-originais", "ferramentas") for parte in p.parts)
    )
    urls = "\n".join(
        f"  <url><loc>{SITE}{'' if c == '.' else c + '/'}</loc></url>" for c in paginas
    )
    return f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
{urls}
</urlset>
"""


def preencher_home():
    """A Home é feita à mão, mas os trechos entre
    <!-- gerado:NOME --> e <!-- /gerado --> são preenchidos aqui."""
    arquivo = RAIZ / "index.html"
    html = arquivo.read_text(encoding="utf-8")
    trechos = {
        "cabeca": cabeca_meta("", "Camila Raposa · Arte é para todos",
                              "Camila Raposa, artista visual e professora de arte em Porto Alegre. Aulas de aquarela, desenho, ilustração e HQ, oficinas e ilustrações sob encomenda.", ""),
        "marca": marca(""),
        "foto-abertura": foto("home-abertura", "", "Foto: Camila pintando", lazy=False),
        "foto-aula": foto("home-aula", "", "Foto: aula na Koralle"),
        "foto-ilustracao": foto("home-ilustracao", "", "Foto: uma ilustração tua"),
        "cartoes": "\n" + cartoes("") + "\n          ",
    }
    for nome, conteudo in trechos.items():
        padrao = re.compile(rf"(<!-- gerado:{nome} -->).*?(<!-- /gerado -->)", re.S)
        if not padrao.search(html):
            raise SystemExit(f"Marcador gerado:{nome} sumiu do index.html da Home.")
        html = padrao.sub(lambda m: m.group(1) + conteudo + m.group(2), html)
    arquivo.write_text(html, encoding="utf-8")


def main():
    registrar_oficinas(OFICINAS)
    novas = preparar_fotos()
    if novas:
        print("Fotos preparadas:", ", ".join(novas))
    pasta = RAIZ / "oficinas"
    pasta.mkdir(exist_ok=True)
    (pasta / "index.html").write_text(pagina_indice_oficinas(), encoding="utf-8")
    for o in OFICINAS:
        p = pasta / o["slug"]
        p.mkdir(exist_ok=True)
        (p / "index.html").write_text(pagina_oficina(o), encoding="utf-8")
    print(f"{len(OFICINAS)} oficinas geradas.")
    from paginas import gerar_paginas
    n = gerar_paginas(RAIZ, topo, rodape, whats)
    print(f"{n} páginas fixas geradas.")
    preencher_home()
    print("Home: trechos marcados atualizados.")
    (RAIZ / "404.html").write_text(pagina_404(), encoding="utf-8")
    (RAIZ / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    print("404.html e sitemap.xml gerados.")


if __name__ == "__main__":
    main()
