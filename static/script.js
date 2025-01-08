function validar() {
    var input1 = document.getElementById("nomeuser").value;
    var botao = document.getElementById("botaoenviar")
    var mensagem = document.getElementById("mensagem");

    if(input1 == ""){
        botao.type = "reset";
        mensagem.textContent = "*O campo nome está vazio";
        mensagem.style.color = "red";
    }else{
        botao.type = "submit";
    }
}