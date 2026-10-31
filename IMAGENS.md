# Imagens do site

Lista de todas as imagens que o site espera.
São 25 no total. Pode mandar aos poucos, na ordem que quiser.

## As 3 formas

- **Em pé**: mais alta que larga. Mínimo 1200 × 1500 pixels.
- **Deitada**: mais larga que alta. Mínimo 1500 × 1000 pixels.
- **Livre**: qualquer forma. Aparece inteira, sem cortar nada.

Foto tirada com o S23 já passa do tamanho mínimo. Não precisa medir.

## Dicas

- Mande a foto original, não print da tela.
- O site corta um pouco das bordas pra caber no espaço. Deixe o mais importante no meio.
- A foto com celular em pé vira "em pé". A foto com celular deitado vira "deitada".
- O gerador tira sozinho a localização (GPS) que o celular grava na foto.

## Marca

1. **Logo da raposa**
   - Onde: topo de todas as páginas, do lado do nome.
   - Forma: livre.
   - Melhor se for PNG com fundo transparente, ou SVG.

2. **Prévia do link**
   - Onde: a imagem que aparece quando alguém manda o link do site no WhatsApp.
   - Forma: deitada, 1200 × 630.
   - Se não tiver uma pronta, eu monto com o logo e uma arte tua.

## Home

3. **Tu pintando**
   - Onde: abertura, do lado do "Arte é para todos". No celular, vem antes do texto.
   - Forma: em pé.

4. **Aula na Koralle**
   - Onde: bloco "Pra aprender".
   - Forma: deitada.
   - Se aparecer rosto de aluno, precisa de autorização. De criança, autorização dos responsáveis.

5. **Uma ilustração forte**
   - Onde: bloco "Pra encomendar".
   - Forma: deitada.

## Sobre

6. **Tu desenhando**
   - Onde: parte "A artista".
   - Forma: em pé.

7. **Tu dando aula**
   - Onde: parte "A Professora Raposa".
   - Forma: em pé.

## Eventos

8. **Aquarela ao vivo**
   - Onde: parte "Aquarela ao vivo".
   - Forma: deitada.

9. **Festa com oficina**
   - Onde: parte "Oficina na sua festa".
   - Forma: deitada.

## Oficinas (uma por oficina)

Todas em pé, com o trabalho bem no meio.
A mesma foto aparece quadrada no cartão e em pé na página da oficina.

10. Aquarela para iniciantes
11. Aquarela flores e frutas
12. Gatitos e aquarela
13. Aquarela de Natal
14. Aquarela de Halloween
15. Lápis de cor aquarelável
16. Marcadores a álcool
17. Lettering sem julgamentos
18. Horror de pintar
19. Gambiarra artística

## Portfólio

20 a 25. **Seis artes tuas**
   - Forma: livre. A arte aparece inteira, sem corte.
   - Mínimo 1200 pixels no lado maior.
   - O resto continua no link do Behance.

---

## Pra quem for encaixar (parte técnica)

1. Salve a original em `fotos-originais/<lugar>.jpg`.
2. Rode `python3 ferramentas/gerar.py`.
3. Confira o texto alternativo (`alt`) em `LUGARES`, no `ferramentas/imagens.py`. Ele deve descrever o que a imagem mostra de verdade.

Nomes dos lugares:
`logo`, `compartilhar`, `home-abertura`, `home-aula`, `home-ilustracao`,
`sobre-artista`, `sobre-professora`, `eventos-aquarela-ao-vivo`, `eventos-festa`,
`oficina-<slug da oficina>` (ex.: `oficina-horror-de-pintar`),
`portfolio-1` até `portfolio-6`.
