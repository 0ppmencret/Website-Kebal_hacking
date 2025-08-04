
from flask import Flask, render_template_string
app = Flask(__name__)

@app.route('/')
def secure_web():
    security_layers = [
        "HTTPS Enforcement", "Content Security Policy", "X-Frame-Options",
        "XSS Filtering", "SQL Injection Prevention", "Rate Limiting",
        "Password Hashing (bcrypt)", "Session Expiry", "Two-Factor Auth",
        "CSRF Tokens", "SameSite Cookies", "Secure Cookies", "HTTPOnly",
        "Firewall Rules", "IP Whitelisting", "Cloudflare Proxy",
        "Input Sanitization", "JWT Signature Check", "Token Expiry",
        "Login Lockout", "Google reCAPTCHA", "Encryption at Rest",
        "Encryption in Transit", "CORS Policy", "Audit Logs", "WAF Integration"
    ]
    while len(security_layers) < 100:
        security_layers.append("Generic Defense Layer #" + str(len(security_layers) + 1))

    return render_template_string("""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>SecureLayer Flask Web</title>
  <style>
    body {
      margin: 0;
      background: #111;
      color: #fff;
      font-family: monospace;
      overflow-x: hidden;
      text-align: center;
    }
    h1 {
      margin: 2rem 0;
      color: #00ffc3;
    }
    .layer {
      margin: 5px auto;
      width: 90%;
      padding: 10px;
      background: rgba(0,255,200,0.05);
      border: 1px solid rgba(0,255,200,0.1);
      border-radius: 8px;
      animation: fadein 1s ease forwards;
    }
    @keyframes fadein {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }
  </style>
</head>
<body>
  <h1>🔐 SecureLayer Flask Web</h1>
  <div id="layers">
    {% for layer in layers %}
      <div class="layer">Layer {{ loop.index }}: {{ layer }}</div>
    {% endfor %}
  </div>
</body>
</html>
""", layers=security_layers)

if __name__ == '__main__':
    app.run(debug=True)
