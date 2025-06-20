const API_URL = "http://localhost:8000/api";

async function ask() {
  const question = document.getElementById("question").value;
  const resBox = document.getElementById("response");
  resBox.innerHTML = "Generating answer...";
  const res = await fetch(`${API_URL}/ask`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json"
    },
    body: JSON.stringify({ question })
  });
  const data = await res.json();
  resBox.innerHTML = `<b>Answer:</b> ${data.answer}`;
}

async function refresh() {
  const resBox = document.getElementById("response");
  resBox.innerHTML = "Refreshing articles...";
  const res = await fetch(`${API_URL}/refresh`);
  const data = await res.json();
  resBox.innerHTML = `✅ ${data.status}`;
}
