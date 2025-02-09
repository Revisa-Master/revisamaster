from flask import Flask, render_template, request, redirect, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os

app = Flask(__name__)
app.secret_key = 'uma_chave_super_secreta'


# Carregar variáveis de ambiente

EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.revisamaster.contato@gmail.com"
EMAIL_HOST_PASSWORD = "nidz gesi ntpi prgx"  # Use a senha de app do Gmail!
RECIPIENT_EMAIL = "a.revisamaster@gmail.com"

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def pagina_inicial():
    return render_template('index.html')

# Rota para a página Sobre
@app.route('/sobre-nos')
def about():
    return render_template('about.html')

# Rota para a página de Serviços
@app.route('/nossos-servicos')
def services():
    return render_template('services.html')

# Rota para a página FAQ
@app.route('/perguntas-frequentes')
def faq():
    return render_template('faq.html')

# Rota para a página de Contato (onde estará o formulário)
@app.route('/contacto')
def contacto():
    return render_template('contacto.html')

@app.route('/enviar_email', methods=['POST'])
def enviar_email():
    try:
        # Capturar os dados do formulário
        nome = request.form['nome']
        email = request.form['email']
        servico = request.form['servico']
        paginas = request.form['paginas']
        prazo = request.form['prazo']
        mensagem = request.form['mensagem']

        # Criar a mensagem do e-mail
        subject = f"Novo contacto de {nome} - {servico}"
        body = f"""
        Nome: {nome}
        E-mail: {email}
        Serviço desejado: {servico}
        Número de páginas: {paginas}
        Prazo: {prazo}

        Mensagem:
        {mensagem}
        """
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = RECIPIENT_EMAIL
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        # Configurar conexão com o servidor SMTP do Gmail
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
        server.sendmail(EMAIL_HOST_USER, RECIPIENT_EMAIL, msg.as_string())
        server.quit()

        flash("E-mail enviado com sucesso!", "success")

    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")
        flash(f"Erro ao enviar o e-mail: {e}", "danger")
    
    return redirect('/contacto')

# Rota para a página de Política de Privacidade
@app.route('/politica-de-privacidade')
def privacy():
    return render_template('privacy.html')

if __name__ == '__main__':
    app.run(debug=True)
