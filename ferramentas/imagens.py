"""
Imagens do site: a lista dos lugares e o preparo das fotos.

Como colocar uma imagem nova:
1. Salve a foto original em  fotos-originais/<nome-do-lugar>.jpg
   (pode ser .jpg, .jpeg, .png, .webp ou .heic).
   O nome do lugar está na lista LUGARES abaixo. Ex.: fotos-originais/home-abertura.jpg
2. Rode:  python3 ferramentas/gerar.py
   O gerador diminui a foto, tira a localização (GPS) e os dados da câmera,
   salva em assets/img/ e troca o quadro rosa pela imagem em todas as páginas.

A pasta fotos-originais/ não vai pro GitHub (está no .gitignore): fotos de celular são pesadas.
Só as versões leves de assets/img/ vão pro site.
"""
from pathlib import Path
from html import escape

from PIL import Image, ImageOps

try:  # fotos .heic do celular; se não tiver a biblioteca, só não lê .heic
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    pass

RAIZ = Path(__file__).resolve().parent.parent
ORIGINAIS = RAIZ / "fotos-originais"
PRONTAS = RAIZ / "assets" / "img"
EXTENSOES = (".jpg", ".jpeg", ".png", ".webp", ".heic")

# forma: "em pé" (4:5), "deitada" (3:2), "quadrada" (1:1), "livre" (não corta nada)
# alt: o que a imagem mostra, pra quem usa leitor de tela. Ajustar quando a foto chegar.
LUGARES = {
    "logo": dict(forma="livre", alt="Camila Raposa", onde="Topo de todas as páginas"),
    "home-abertura": dict(forma="em pé", alt="Camila Raposa pintando", onde="Home, abertura"),
    "home-aula": dict(forma="deitada", alt="Aula de arte na Koralle", onde="Home, bloco Pra aprender"),
    "home-ilustracao": dict(forma="deitada", alt="Ilustração da Camila Raposa", onde="Home, bloco Pra encomendar"),
    "sobre-artista": dict(forma="em pé", alt="Camila Raposa desenhando", onde="Sobre, A artista"),
    "sobre-professora": dict(forma="em pé", alt="Camila Raposa dando aula", onde="Sobre, A Professora Raposa"),
    "eventos-aquarela-ao-vivo": dict(forma="deitada", alt="Camila pintando aquarela ao vivo num evento", onde="Eventos, Aquarela ao vivo"),
    "eventos-festa": dict(forma="deitada", alt="Festa de aniversário com oficina de arte", onde="Eventos, Oficina na sua festa"),
    "compartilhar": dict(forma="1200x630", alt="Camila Raposa, artista visual e professora de arte", onde="Prévia quando mandam o link no WhatsApp"),
}
for i in range(1, 7):
    LUGARES[f"portfolio-{i}"] = dict(forma="livre", alt=f"Arte {i} do portfólio da Camila Raposa", onde="Portfólio")
# Oficinas: uma foto em pé por oficina (o slug vem do gerar.py).
# Ela aparece quadrada no cartão (corta o meio) e em pé na página da oficina.

TAMANHOS = (800, 1600)  # largura das versões leves


def registrar_oficinas(oficinas):
    for o in oficinas:
        LUGARES.setdefault(
            f"oficina-{o['slug']}",
            dict(forma="em pé", alt=f"Trabalhos da oficina {o['nome']}", onde=f"Oficina {o['nome']}"),
        )


def _original(lugar):
    for ext in EXTENSOES:
        for p in (ORIGINAIS / f"{lugar}{ext}", ORIGINAIS / f"{lugar}{ext.upper()}"):
            if p.exists():
                return p
    return None


def preparar_fotos():
    """Transforma cada foto de fotos-originais/ em versões leves em assets/img/."""
    if not ORIGINAIS.exists():
        return []
    PRONTAS.mkdir(parents=True, exist_ok=True)
    feitas = []
    for lugar in LUGARES:
        orig = _original(lugar)
        if not orig:
            continue
        destino = PRONTAS / ("compartilhar.jpg" if lugar == "compartilhar" else f"{lugar}-800.webp")
        if destino.exists() and destino.stat().st_mtime >= orig.stat().st_mtime:
            continue  # já está pronta
        im = ImageOps.exif_transpose(Image.open(orig))  # endireita foto deitada do celular
        transparente = im.mode in ("RGBA", "LA") or (im.mode == "P" and "transparency" in im.info)
        im = im.convert("RGBA" if transparente else "RGB")  # logo em PNG mantém o fundo transparente
        for p in PRONTAS.glob(f"{lugar}-*"):
            p.unlink()  # versões antigas da mesma foto
        if lugar == "compartilhar":
            ImageOps.fit(im.convert("RGB"), (1200, 630)).save(PRONTAS / "compartilhar.jpg", quality=85, optimize=True)
            feitas.append(lugar)
            continue
        for largura in TAMANHOS:
            if largura != TAMANHOS[0] and im.width <= TAMANHOS[0]:
                break  # foto pequena: a versão grande seria igual à pequena
            copia = im.copy()
            if copia.width > largura:
                copia.thumbnail((largura, largura * 10), Image.LANCZOS)
            copia.save(PRONTAS / f"{lugar}-{largura}.webp", quality=82, method=6)
        feitas.append(lugar)
    return feitas


def existe(lugar):
    if lugar == "compartilhar":
        return (PRONTAS / "compartilhar.jpg").exists()
    return (PRONTAS / f"{lugar}-800.webp").exists()


CLASSE_FORMA = {"em pé": "", "deitada": " foto--larga", "quadrada": " foto--quadrada", "livre": " foto--livre"}


def foto(lugar, r, rotulo, forma=None, tag="div", lazy=True):
    """A imagem, se já chegou. Se não, o quadro rosa com o rótulo."""
    info = LUGARES[lugar]
    forma = forma or info["forma"]
    classe = CLASSE_FORMA.get(forma, "")
    if not existe(lugar):
        if tag == "span":
            return f'<span class="foto{classe}">{escape(rotulo)}</span>'
        return f'<div class="foto{classe}" role="img" aria-label="Lugar reservado. {escape(rotulo)}">{escape(rotulo)}</div>'
    versoes = sorted(PRONTAS.glob(f"{lugar}-*.webp"), key=lambda p: int(p.stem.rsplit("-", 1)[1]))
    menor = versoes[0]
    with Image.open(menor) as im:
        w, h = im.size
    srcset = ", ".join(f'{r}assets/img/{p.name} {Image.open(p).width}w' for p in versoes)
    carregar = ' loading="lazy"' if lazy else ' fetchpriority="high"'
    return (
        f'<img class="foto-img{classe}" src="{r}assets/img/{menor.name}" srcset="{srcset}" '
        f'sizes="(min-width: 56rem) 40vw, 100vw" width="{w}" height="{h}" '
        f'alt="{escape(info["alt"])}"{carregar} decoding="async">'
    )
