// Abre e fecha o menu no celular.
(function () {
  var botao = document.querySelector('.botao-menu');
  var menu = document.getElementById('menu');
  if (!botao || !menu) return;
  botao.addEventListener('click', function () {
    var aberto = menu.classList.toggle('aberto');
    botao.setAttribute('aria-expanded', aberto ? 'true' : 'false');
    botao.textContent = aberto ? 'Fechar' : 'Menu';
  });
})();
