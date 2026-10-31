"""
Páginas fixas do site (tudo que não é oficina).
É chamado pelo gerar.py. Pra mudar um texto, mude aqui e rode:
    python3 ferramentas/gerar.py
"""


def gerar_paginas(raiz, topo, rodape, whats):
    r = "../"

    def botao_whats(texto_botao, mensagem, extra=""):
        return f'<a class="botao botao--whats{extra}" href="{whats(mensagem)}">{texto_botao}</a>'

    def foto(rotulo, classe=""):
        return f'<div class="foto{classe}" role="img" aria-label="Lugar da foto: {rotulo}">Foto: {rotulo}</div>'

    def cabeca(titulo, frase):
        return f"""
    <section class="pagina-topo">
      <div class="miolo">
        <h1>{titulo}</h1>
        <p class="pagina-frase">{frase}</p>
      </div>
    </section>
"""

    paginas = {}

    # ---------------- AULAS ----------------
    paginas["aulas"] = (
        "Aulas",
        "Aulas de arte presenciais na Koralle, em Porto Alegre, e online ao vivo. Aquarela, desenho, ilustração, quadrinhos e personagens.",
        cabeca("Aulas", "No seu tempo, do seu jeito. Sem pressa e sem prazo pra terminar.") + f"""
    <section class="secao">
      <div class="miolo">
        <div class="duas-aulas">
          <div class="aula">
            <h2>Presencial na Koralle</h2>
            <p>Aulas em grupo, com acompanhamento de perto e muito material pra experimentar.</p>
            <dl class="fatos">
              <div><dt>Quando</dt><dd>Terças. Turma da manhã, das 9h às 11h. Turma da tarde, das 15h às 17h.</dd></div>
              <div><dt>Onde</dt><dd>Koralle, Av. José Bonifácio, 95, Farroupilha, Porto Alegre</dd></div>
              <div><dt>Idade</dt><dd>A partir de 8 anos</dd></div>
              <div><dt>Inclui</dt><dd>Todo o material da aula e certificado</dd></div>
            </dl>
            {botao_whats("Quero uma vaga na Koralle", "Oi, Camila! Quero saber das aulas presenciais na Koralle.")}
          </div>
          <div class="aula">
            <h2>Online ao vivo</h2>
            <p>Aulas particulares pelo Zoom. Você escolhe o que quer aprender e eu acompanho no seu ritmo.</p>
            <dl class="fatos">
              <div><dt>Quando</dt><dd>Quintas, horário a combinar</dd></div>
              <div><dt>Onde</dt><dd>Pelo Zoom, de onde você estiver</dd></div>
              <div><dt>Idade</dt><dd>A partir de 5 anos</dd></div>
              <div><dt>Pra começar</dt><dd>O primeiro encontro é grátis: 30 minutos pra conhecer o jeito da aula e tirar dúvidas</dd></div>
            </dl>
            {botao_whats("Quero meu encontro grátis", "Oi, Camila! Quero marcar o encontro grátis da aula online.")}
          </div>
        </div>
      </div>
    </section>

    <section class="secao secao--rosa">
      <div class="miolo">
        <h2>O que dá pra aprender</h2>
        <ul class="temas">
          <li><strong>Aquarela.</strong> Do básico ao avançado, com fluidez e cor.</li>
          <li><strong>Desenho básico.</strong> Estrutura, formas e observação.</li>
          <li><strong>Desenho pra crianças.</strong> Leve, brincado e cheio de estímulo.</li>
          <li><strong>Ilustração tradicional.</strong> Lápis, nanquim, canetas e mais.</li>
          <li><strong>Ilustração digital.</strong> Procreate, Krita ou Photoshop. Só online.</li>
          <li><strong>Histórias em quadrinhos e mangá.</strong> Narrativa, personagens e sequência.</li>
          <li><strong>Criação de personagens.</strong> Do rascunho à personalidade.</li>
          <li><strong>Projeto parado.</strong> Apoio pra tirar do papel aquela ideia que está na gaveta.</li>
        </ul>
      </div>
    </section>

    <section class="secao">
      <div class="miolo faixa">
        <h2>Cada cabeça aprende de um jeito</h2>
        <div>
          <p>Tenho experiência com alunos autistas, com TDAH e com altas habilidades. A aula se ajusta a quem está aprendendo.</p>
          <a class="botao botao--petroleo" href="{r}psicopedagogia/">Conhecer a psicopedagogia</a>
        </div>
      </div>
    </section>
""",
    )

    # ---------------- SOBRE ----------------
    paginas["sobre"] = (
        "Sobre",
        "Camila Raposa: artista visual formada pela UFPel e professora de arte em Porto Alegre.",
        cabeca("Sobre", "Artista que ensina, professora que cria.") + f"""
    <section class="secao">
      <div class="miolo colunas">
        <div>
          <h2>A artista</h2>
          <p>Meu trabalho traz referências da cultura pop, da moda e do mundo geek e nerd, em personagens diversos e divertidos.</p>
          <p>Também tenho um trabalho voltado ao terror, que me orgulha muito.</p>
          <p>Sou formada em Artes Visuais pela UFPel. Desde então, fiz design de personagens, quadrinhos, livros ilustrados, estamparia e muito mais.</p>
          <p>Trabalho de forma independente e colaboro com agências em projetos grandes e pequenos. Já desenhei para Microsoft, Facebook, Caderno Inteligente, Pentel e New Pen.</p>
          <p>Moro em Porto Alegre.</p>
          <a class="botao botao--petroleo" href="{r}portfolio/">Ver o portfólio</a>
        </div>
        <div>{foto("Camila desenhando")}</div>
      </div>
    </section>

    <section class="secao secao--rosa">
      <div class="miolo colunas">
        <div>
          <h2>A Professora Raposa</h2>
          <p>Ensino técnicas artísticas, principalmente desenho, aquarela, ilustração e animação.</p>
          <p>Tenho experiência com pessoas neurodivergentes, em especial alunos autistas, com TDAH e com altas habilidades.</p>
          <p>Busco criar um espaço acessível e acolhedor, onde cada aluno explora a criatividade do seu jeito e no seu ritmo.</p>
          <p>Pra mim, a arte é uma linguagem: uma ponte entre o mundo de dentro e o de fora. O desenho, os quadrinhos e a animação ajudam a construir autonomia, escuta e sentido.</p>
          <p>Hoje curso pós-graduação em Psicopedagogia, pra entender cada vez melhor como a gente aprende.</p>
          <a class="botao botao--petroleo" href="{r}aulas/">Conhecer as aulas</a>
        </div>
        <div>{foto("Camila dando aula")}</div>
      </div>
    </section>
""",
    )

    # ---------------- PSICOPEDAGOGIA ----------------
    paginas["psicopedagogia"] = (
        "Psicopedagogia",
        "Camila Raposa e a psicopedagogia: arte e aprendizagem para cabeças diferentes.",
        cabeca("Psicopedagogia", "Cada cabeça aprende de um jeito.") + f"""
    <section class="secao">
      <div class="miolo">
        <p>Curso pós-graduação em Psicopedagogia e estudo como a gente aprende, e as muitas formas de mostrar o que aprendeu.</p>
        <p>Na sala de aula, isso já aparece: tenho experiência com alunos autistas, com TDAH e com altas habilidades.</p>
        <p>Em breve conto mais por aqui. Se quiser conversar antes, me chama.</p>
        {botao_whats("Conversar no WhatsApp", "Oi, Camila! Quero saber mais sobre o teu trabalho com psicopedagogia.")}
      </div>
    </section>
""",
    )

    # ---------------- PORTFÓLIO ----------------
    artes = "\n".join(
        f'          <li><div class="foto foto--quadrada" role="img" aria-label="Lugar da arte {i}">Arte {i}</div></li>'
        for i in range(1, 7)
    )
    paginas["portfolio"] = (
        "Portfólio",
        "Portfólio da Camila Raposa: personagens, quadrinhos, livros ilustrados e terror. Ilustração sob encomenda.",
        cabeca("Portfólio", "Personagens, quadrinhos, livros ilustrados e terror.") + f"""
    <section class="secao">
      <div class="miolo">
        <ul class="galeria">
{artes}
        </ul>
        <a class="botao botao--petroleo" href="https://www.behance.net/camilaraposaarte">Ver o portfólio completo no Behance</a>
      </div>
    </section>

    <section class="secao secao--rosa" id="encomendas">
      <div class="miolo">
        <h2>Encomende uma arte</h2>
        <p>Faço ilustração sob encomenda pra pessoas, editoras e marcas: personagens, livros, quadrinhos e estampas.</p>
        <p>Me conta a ideia, o prazo e onde a arte vai ser usada. Eu respondo com um orçamento.</p>
        {botao_whats("Pedir orçamento", "Oi, Camila! Quero pedir um orçamento de ilustração.")}
      </div>
    </section>
""",
    )

    # ---------------- EVENTOS ----------------
    paginas["eventos"] = (
        "Eventos",
        "Aquarela ao vivo e oficinas de arte para festas e eventos em Porto Alegre, com a Camila Raposa.",
        cabeca("Eventos", "Arte ao vivo, no seu evento ou no meu.") + f"""
    <section class="secao">
      <div class="miolo colunas">
        <div>
          <h2>Aquarela ao vivo</h2>
          <p>Pinto retratos em aquarela ao vivo, durante o seu evento. Cada convidado leva o seu pra casa.</p>
          <p>Funciona em casamento, aniversário, lançamento de produto e ação de marca.</p>
          {botao_whats("Pedir orçamento", "Oi, Camila! Quero um orçamento de aquarela ao vivo pro meu evento.")}
        </div>
        <div>{foto("aquarela ao vivo", " foto--larga")}</div>
      </div>
    </section>

    <section class="secao secao--rosa">
      <div class="miolo colunas">
        <div>
          <h2>Oficina na sua festa</h2>
          <p>Qualquer oficina pode virar festa de aniversário, pra criança ou pra adulto. Eu levo o material e conduzo a atividade.</p>
          {botao_whats("Quero uma festa assim", "Oi, Camila! Quero saber da oficina pra festa de aniversário.")}
        </div>
        <div>{foto("festa com oficina", " foto--larga")}</div>
      </div>
    </section>

    <section class="secao">
      <div class="miolo">
        <h2>Onde me encontrar</h2>
        <p>Lançamentos de livro, feiras e eventos na Koralle. As próximas datas saem aqui e no Instagram.</p>
        <a class="botao botao--petroleo" href="https://www.instagram.com/camilaraposa/">Seguir no Instagram</a>
      </div>
    </section>
""",
    )

    # ---------------- MATERIAIS ----------------
    paginas["materiais"] = (
        "Lista de materiais",
        "Os materiais de arte que a Camila Raposa usa e indica, pra começar sem gastar à toa.",
        cabeca("Lista de materiais", "O que eu uso e indico, pra começar sem gastar à toa.") + f"""
    <section class="secao">
      <div class="miolo">
        <h2>Pra começar na aquarela</h2>
        <dl class="fatos">
          <div><dt>Pincel</dt><dd>Giotto, nº 6 ou nº 8. É o mais barato que é bom de verdade.</dd></div>
          <div><dt>Papel</dt><dd>Montval grain fin, da Canson. É o que eu uso nas oficinas. Tem na Koralle.</dd></div>
          <div><dt>Tinta</dt><dd>Uma cartela de amostras já basta pra testar as cores antes de comprar o estojo.</dd></div>
        </dl>
        <p class="nota">Mais materiais e links de compra entram aqui em breve.</p>
      </div>
    </section>
""",
    )

    # ---------------- CONTATO ----------------
    paginas["contato"] = (
        "Contato",
        "Fale com a Camila Raposa pelo WhatsApp: aulas, oficinas, orçamentos e eventos.",
        cabeca("Contato", "O jeito mais rápido de falar comigo é pelo WhatsApp.") + f"""
    <section class="secao">
      <div class="miolo">
        <p>Escolha o assunto. A mensagem já vai pronta, é só enviar.</p>
        <ul class="assuntos">
          <li>{botao_whats("Quero agendar uma aula", "Oi, Camila! Quero agendar uma aula.")}</li>
          <li>{botao_whats("Quero saber de uma oficina", "Oi, Camila! Quero saber das oficinas.")}</li>
          <li>{botao_whats("Quero pedir um orçamento", "Oi, Camila! Quero pedir um orçamento.")}</li>
          <li>{botao_whats("Quero falar de outra coisa", "Oi, Camila!")}</li>
        </ul>
        <p>WhatsApp: <a href="https://wa.me/5551989201232">(51) 98920-1232</a></p>
        <p>Às terças estou dando aula na Koralle. Mensagem que chega na terça, eu respondo na quarta.</p>
      </div>
    </section>
""",
    )

    for slug, (titulo, desc, corpo) in paginas.items():
        pasta = raiz / slug
        pasta.mkdir(exist_ok=True)
        (pasta / "index.html").write_text(
            topo(r, titulo, desc, slug) + corpo + rodape(r), encoding="utf-8"
        )
    return len(paginas)
