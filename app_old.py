from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nome: str = request.form['nome']
        email: str = request.form['email']

        # Para fazer algo com os dados, como salvar em um banco de dados, enviar um email, etc.
        return f'Obrigado, {nome}! Seu email {email} foi registrado.'
    else:
        return render_template('form.html')


app.route('/index')


def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
