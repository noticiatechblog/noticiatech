(function () {
  function setMessage(form, message, state) {
    var target = form.querySelector("[data-newsletter-message]");
    if (!target) return;
    target.textContent = message;
    target.dataset.state = state || "";
  }

  document.addEventListener("submit", function (event) {
    var form = event.target;
    if (!form.matches("[data-newsletter-form]")) return;

    event.preventDefault();

    var button = form.querySelector("button[type='submit']");
    var data = new URLSearchParams(new FormData(form));

    if (button) button.disabled = true;
    setMessage(form, "Enviando cadastro...", "loading");

    fetch(form.action, {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/x-www-form-urlencoded"
      },
      body: data.toString()
    })
      .then(function (response) {
        return response.json().catch(function () {
          return {};
        }).then(function (body) {
          if (!response.ok) {
            throw new Error(body.error || "Nao foi possivel cadastrar agora.");
          }
          return body;
        });
      })
      .then(function () {
        form.reset();
        setMessage(form, "Cadastro recebido. Obrigado!", "success");
      })
      .catch(function (error) {
        setMessage(form, error.message, "error");
      })
      .finally(function () {
        if (button) button.disabled = false;
      });
  });
})();
