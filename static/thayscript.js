const paragrafo = document.getElementById('turma');

const botao = document.getElementById('clicar');
const input = document.getElementById('texto');

botao.addEventListener('click', function() {

    //paragrafo.textContent = paragrafo.textContent + input.value;
    paragrafo.innerHTML = paragrafo.innerHTML + '<br>' + input.value;
    paragrafo.style.backgroundColor = rgb(11, 66, 32);
}
 );

 function entrar() {
    var input1 = document.getElementById("senha1").value;
    var input2 = document.getElementById("senha2").value;
    var mensagem = document.getElementById("mensagem");

    if (senha1 == ""){
        mensagem.textContent= "Resposta vazia. Preencha corretamente.";
        mensagem.style.color = "red";
    }else if(senha2 == ""){
        mensagem.textContent= "Resposta vazia. Preencha corretamente.";
        mensagem.style.color= "red";
    }
    if (input1 === input2) {
        mensagem.textContent = "Senha correta.";
        mensagem.style.color = "green";
    } else {
        mensagem.textContent = "Senha incorreta";
        mensagem.style.color = "red";
    }
}

