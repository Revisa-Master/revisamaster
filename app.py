from flask import Flask, render_template, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)

# Carregar variáveis de ambiente

EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
RECIPIENT_EMAIL = os.getenv('RECIPIENT_EMAIL')

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/index')
def pagina_inicial():
    return render_template('index.html')

# Rota para a página Sobre
@app.route('/about')
def about():
    return render_template('about.html')

# Rota para a página de Serviços
@app.route('/services')
def services():
    return render_template('services.html')

# Rota para a página FAQ
@app.route('/faq')
def faq():
    return render_template('faq.html')

# Rota para a página de Contato (onde estará o formulário)
@app.route('/contato')
def contact():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)
