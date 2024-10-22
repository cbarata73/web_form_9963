from flask import Flask, render_template, request

app = Flask(__name__)

# Rota para a página inicial (index.html)


@app.route('/')
def index():
    return render_template('index.html')


# Rota para a página de contactos (contactos.html)
@app.route('/contactos')
def contactos():
    return render_template('contactos.html')


# Rota para o formulário (form.html)
@app.route('/form')
def form() -> str:
    return render_template('form.html')


# Rota para capturar os dados do formulário
@app.route('/submit', methods=['POST'])
def submit_form() -> str:
    nome: str = request.form['nome']
    email: str = request.form['email']
    # nome= request.args.get('nome')
    # email = request.args.get('email')

    # Exibir os dados no console (ou guardar numa base de dados)
    print(f'Nome: {nome}')
    print(f'Email: {email}')
    return f"Dados recebidos!<br/><br/>Nome: {nome}<br/> Email: {email}"


# Rota para a página de multimédia (multimedia.html)
@app.route('/multimedia')
def multimedia() -> str:
    return render_template('multimedia.html')


if __name__ == '__main__':
    #app.run(debug=True)
    app.run()
    