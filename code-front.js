document.addEventListener("keypress", function(e) {
    if (e.key === 'Enter') {
        var botao = document.querySelector("#botaoEnviar");
        botao.click();
    }
});
