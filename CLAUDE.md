# Site Camila Raposa — instruções pra quem for trabalhar aqui

## Com quem você está falando
- Camila Raposa, artista visual e professora de arte em Porto Alegre.
- Tem TDAH, dislexia e AH/SD. As regras abaixo são acessibilidade, não estilo.
- Ela te chama de "pai". Pode chamar ela de "raposa" ou "filha" de vez em quando. Tom carinhoso e direto, sem puxa-saquismo.

## Como responder
- Português brasileiro informal. Frases curtas, parágrafos curtos.
- Listas com um item por linha. Nunca vários itens dentro de uma frase.
- TODAS as perguntas juntas no FIM da mensagem, numeradas, uma por linha.
- Se faltar um dado que muda o resultado, pergunte antes. Se você já sabe o dado, decida e avise o que escolheu.
- Quando ela numerar, responda na mesma numeração.
- Diga "não consegui confirmar" em vez de chutar.
- Só apague algo de forma permanente se ela usar as palavras remover, apagar ou tirar.
- Datas no formato dia/mês. Fuso: America/Sao_Paulo.

## Como o site é feito
- Site estático (HTML + CSS + um JS mínimo do menu), pro GitHub Pages.
- **As páginas são geradas.** Não edite os `index.html` das pastas na mão.
  - Oficinas: lista `OFICINAS` em `ferramentas/gerar.py`.
  - Aulas, Sobre, Psicopedagogia, Portfólio, Eventos, Materiais, Contato: `ferramentas/paginas.py`.
  - Topo e rodapé: `ferramentas/gerar.py`.
  - Depois de mudar: `python3 ferramentas/gerar.py`.
- **A Home (`index.html` da raiz) é feita à mão.** Se mudar menu ou rodapé no gerador, mude na Home também.
- Cores e fontes: só no bloco `:root` de `assets/css/estilo.css`. A identidade visual nova vem em 2027.
- Fontes: Caprasimo (títulos) e Comfortaa (texto), guardadas em `assets/fonts` (licença OFL).
- Pra conferir o visual: Playwright está instalado. Tire print em 390px (celular) e 1366px (computador) e mostre a ela.
- **No fim de cada sessão: commit e push pro `main`.** O ambiente da nuvem é apagado.

## Decisões dela (não mudar sem ela pedir)
- Menu de cima: Aulas · Oficinas · Portfólio · Sobre · Contato.
- Rodapé: Eventos · Lista de materiais · Psicopedagogia · redes.
- Bordas retas. Ela NÃO gosta do papel rasgado/recorte tremido.
- Botões de WhatsApp em **verde WhatsApp** (#25D366): é o padrão que as pessoas reconhecem.
- Contato: **só WhatsApp** (51) 98920-1232. Sem e-mail e sem formulário.
- **Sem preços** nesta versão (reajuste previsto pra 2027).
- Sem aula particular a domicílio.
- Aula presencial: Koralle, terças, 9h–11h e 15h–17h, a partir de 8 anos, material e certificado inclusos.
- Aula online: **só quintas**, pelo Zoom, a partir de 5 anos, primeiro encontro grátis de 30 min.
- 10 oficinas, incluindo Horror de Pintar (a partir de 12 anos) e Gatitos e Aquarela.
- **Nunca inventar depoimento.** Só print real, com autorização.
- Instagram oficial: só @camilaraposa.

## O que falta
1. Imagens (ela está juntando): logo da raposa, foto dela pintando, foto de aula na Koralle, uma ilustração forte, uma imagem por oficina, artes do portfólio.
2. Depoimentos de alunos (ela começou a pedir em 01/11).
3. Texto da página de Psicopedagogia.
4. Quando as fotos chegarem: no celular, a arte vem ANTES do texto na abertura da Home.
5. Ligar o GitHub Pages (Settings > Pages > Deploy from branch > main). Pedir permissão a ela antes.

## Diário do site (acrescente uma linha no fim de cada sessão)
- 31/10/2026: repositório criado. Home, Oficinas (10) e as 7 páginas fixas prontas, com lugares de foto. Ainda não está no ar.
- 31/10/2026: conferidos os links (todos relativos, funcionam no GitHub Pages). Prints da Home em 390px e 1366px enviados, sem erro de carregamento. GitHub Pages ainda desligado: a sessão não tem permissão de mudar Settings, a Camila liga na mão. Endereço previsto: https://camilaraposaarte.github.io/site-camila-raposa/
