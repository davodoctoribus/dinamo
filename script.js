async function sendMessage() {
  const input = document.getElementById("userInput");
  const message = input.value.trim();
  if (!message) return;

  // mensagem do user
  addMessage(message, "user");
  input.value = "";

  // chamada ao backend (Flash)
  try {
    const response = await fetch("http://127.0.0.1:5000/chat", {
      method: "POST",
      headers: {"Content-Type": "application/json"},
      body: JSON.stringify({pergunta: message})
    });
    const data = await response.json();
    addMessage(data.resposta, "bot");
  } catch (error) {
    addMessage("Não foi possível conectar ao servidor", "bot");
  }
}

function addMessage(text, sender) {
  const chat = document.getElementById("chat");
  const msg = document.createElement("div");
  msg.classList.add("message", sender);
  msg.innerText = text;
  chat.appendChild(msg);
  chat.scrollTop = chat.scrollHeight;
}

document.addEventListener("keypress", function(e) {
    if (e.key === 'Enter') {
        var botao = document.querySelector("#botaoEnviar");
        botao.click();
    }
});
