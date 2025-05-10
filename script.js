// Pega o elemento da tela (display)
const display = document.getElementById("display");

// Função para adicionar número ou operador na tela
function adicionar(valor) {
    vibrarLeve();
  if (display.innerText === "0") {
    display.innerText = valor; // Se a tela só tem zero, troca direto
  } else {
    display.innerText += valor; // Senão, adiciona ao que já tem
  }
}

function vibrarLeve() {
    if (navigator.vibrate) {
      navigator.vibrate(10); // 10 milissegundos, bem suave
    }
  }  
// Função para limpar tudo
function limpar() {
    vibrarLeve();
  display.innerText = "0"; // Volta pro zero bonitão
}

// Função para apagar o último caractere
function voltar() {
    vibrarLeve();
  let texto = display.innerText;
  if (texto.length > 1) {
    display.innerText = texto.slice(0, -1); // Remove o último
  } else {
    display.innerText = "0"; // Se sobrou só 1, volta pro zero
  }
}

// Função para calcular o resultado
function calcular() {
    vibrarLeve();
  try {
    display.innerText = eval(display.innerText); 
    // Usa a função eval pra calcular a expressão como string (tipo "2+2" => 4)
  } catch (error) {
    display.innerText = "Erro"; // Se digitar algo errado, mostra erro
  }
}
