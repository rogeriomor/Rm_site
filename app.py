#from pickle import TRUE
from crypt import methods
from flask import Flask, render_template, redirect, request,
from flask_mail import Mail, Message
from config import email, senha


app=Flask(__name__)
app.secret_key = 'Guta1nina2@@@'

mail_settings= {
    "MAIL_SERVER":"smtp.gmail.com",
    "MAIL_PORT":465,
    "MAIL_USE_TLS":False,
    "MAIL_USE_SSL":True,
    "MAIL_USERNAME":email,
    "MAIL_PASSWORD":senha,
}

app.config.update(mail_settings)
mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem=mensagem

@app.route('/send', methods=['GET','POS¨T'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )
        msg =Message(
            subject=f'{formContato.nome} te enviou uma mensagem no portfolio',
            sender= app.config.get("MAIL_USERNAME"),
            recipients=['rogeriol17q2@gmail.com',app.config.get("MAIL_USERNAME")],
            body=f'''
            f'{formContato.nome} com o email {formContato.email}, te enviou a segunte mensagem:
            {formContato.mensagem}
            '''
            
        )
        flash('Mensagem enviada com sucesso!')
    return redirect('/')

    

@app.route('/')
def index():
    return render_template ('index.html')

if __name__ == '__main__':
    app.run(debug=True)

