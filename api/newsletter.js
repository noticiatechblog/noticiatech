const EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

function readBody(req) {
  if (req.body && typeof req.body === "object") return req.body;

  if (typeof req.body !== "string") return {};

  const contentType = req.headers["content-type"] || "";

  if (contentType.includes("application/json")) {
    try {
      return JSON.parse(req.body);
    } catch {
      return {};
    }
  }

  if (contentType.includes("application/x-www-form-urlencoded")) {
    return Object.fromEntries(new URLSearchParams(req.body));
  }

  return {};
}

function escapeHtml(value) {
  return String(value)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

async function sendWithResend({ email, source }) {
  const apiKey = process.env.RESEND_API_KEY;
  const to = process.env.NEWSLETTER_TO || "newsletter@noticiatech.com.br";
  const from = process.env.NEWSLETTER_FROM || "Noticia Tech <newsletter@noticiatech.com.br>";

  if (!apiKey) {
    return { skipped: true, reason: "missing RESEND_API_KEY" };
  }

  const response = await fetch("https://api.resend.com/emails", {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      from,
      to,
      reply_to: email,
      subject: "Novo cadastro na newsletter",
      html: [
        "<h2>Novo cadastro na newsletter</h2>",
        `<p><strong>Email:</strong> ${escapeHtml(email)}</p>`,
        `<p><strong>Origem:</strong> ${escapeHtml(source || "site")}</p>`,
        `<p><strong>Data:</strong> ${escapeHtml(new Date().toISOString())}</p>`
      ].join("")
    })
  });

  if (!response.ok) {
    const details = await response.text().catch(() => "");
    throw new Error(details || "Resend request failed");
  }

  return response.json().catch(() => ({}));
}

async function saveResendContact(email) {
  const apiKey = process.env.RESEND_API_KEY;
  const audienceId = process.env.RESEND_AUDIENCE_ID;

  if (!apiKey || !audienceId) {
    return { skipped: true };
  }

  const response = await fetch(`https://api.resend.com/audiences/${audienceId}/contacts`, {
    method: "POST",
    headers: {
      Authorization: `Bearer ${apiKey}`,
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      email,
      unsubscribed: false
    })
  });

  if (response.status === 409) return { duplicate: true };

  if (!response.ok) {
    const details = await response.text().catch(() => "");
    throw new Error(details || "Resend contact request failed");
  }

  return response.json().catch(() => ({}));
}

module.exports = async function handler(req, res) {
  res.setHeader("Cache-Control", "no-store");

  if (req.method === "OPTIONS") {
    res.setHeader("Allow", "POST, OPTIONS");
    return res.status(204).end();
  }

  if (req.method !== "POST") {
    res.setHeader("Allow", "POST, OPTIONS");
    return res.status(405).json({ error: "Metodo nao permitido." });
  }

  const body = readBody(req);
  const email = String(body.email || "").trim().toLowerCase();
  const website = String(body.website || "").trim();

  if (website) {
    return res.status(200).json({ ok: true });
  }

  if (!EMAIL_RE.test(email)) {
    return res.status(400).json({ error: "Informe um email valido." });
  }

  try {
    const emailResult = await sendWithResend({
      email,
      source: req.headers.referer || req.headers.origin || "noticiatech.com.br"
    });

    let contactResult = { skipped: true };
    try {
      contactResult = await saveResendContact(email);
    } catch (contactError) {
      console.error("newsletter contact save failed", contactError);
    }

    if (emailResult.skipped && contactResult.skipped) {
      return res.status(503).json({
        error: "Newsletter ainda nao configurada na Vercel."
      });
    }

    return res.status(200).json({ ok: true });
  } catch (error) {
    console.error("newsletter signup failed", error);
    return res.status(502).json({
      error: "Nao foi possivel cadastrar agora. Tente novamente em instantes."
    });
  }
};
