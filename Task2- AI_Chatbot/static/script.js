document.getElementById("send-btn").addEventListener("click", sendMessage);
document.getElementById("user-input").addEventListener("keypress", function (e) {
  if (e.key === "Enter") {
    sendMessage();
  }
});

function sendMessage() {
  const inputField = document.getElementById("user-input");
  const userText = inputField.value.trim();
  if (userText === "") return;

  addMessage(userText, "user");
  inputField.value = "";

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: userText })
  })
    .then(response => response.json())
    .then(data => {
      addMessage(data.reply, "bot");
    })
    .catch(error => {
      addMessage("Error: Cannot connect to server.", "bot");
      console.error(error);
    });
}

function addMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);
  messageDiv.textContent = text;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
