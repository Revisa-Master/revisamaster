from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os

app = Flask(__name__)
app.secret_key = 'uma_chave_super_secreta'
load_dotenv(dotenv_path='.env')

# Carregar variáveis de ambiente
app.config['MAIL_SERVER'] = os.getenv('EMAIL_HOST')
app.config['MAIL_PORT'] = os.getenv('EMAIL_PORT')
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv('EMAIL_HOST_USER')
app.config['MAIL_PASSWORD'] = os.getenv('EMAIL_HOST_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('EMAIL_HOST_USER')

mail = Mail(app)

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
        servico = request.form.getlist('servico')
        paginas = request.form['paginas']
        prazo = request.form['prazo']
        mensagem = request.form['mensagem']

        servico_str = ', '.join(servico) if servico else 'Nenhum serviço selecionado'
        
        # Criar a mensagem do e-mail
        subject = f"Novo contacto de {nome}"
        body = f"""
        Nome: {nome}
        E-mail: {email}
        Serviço desejado: {servico_str}
        Número de páginas: {paginas}
        Prazo: {prazo}

        Mensagem:
        {mensagem}
        """
        with mail.connect() as conn:
            msg = Message(subject, sender=email, recipients=[os.getenv('RECIPIENT_EMAIL')], body=body)
            conn.send(msg)

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
