from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de contatos
contatos = []

@app.route('/')
def index():
    """
    Rota principal que renderiza a página inicial com a lista de contatos.
    """
    return render_template('index.html', contatos=contatos)

@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    """
    Rota para adicionar um novo contato.
    Se o método for POST, adiciona o novo contato à lista.
    Se não, exibe o formulário para adicionar um novo contato.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        favorito = 'favorito' in request.form
        codigo = len(contatos)
        contatos.append([codigo, nome, telefone, email, favorito])
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        return render_template('adicionar_contato.html')  # Renderiza o formulário de adicionar contato

@app.route('/editar_contato/<int:codigo>', methods=['GET', 'POST'])
def editar_contato(codigo):
    """
    Rota para editar um contato existente.
    Se o método for POST, atualiza os detalhes do contato com o ID fornecido.
    Caso contrário, exibe o formulário preenchido com os detalhes do contato para edição.
    """
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        favorito = 'favorito' in request.form
        contatos[codigo] = [codigo, nome, telefone, email, favorito]
        return redirect('/')  # Redireciona de volta para a página inicial
    else:
        contato = contatos[codigo]
        return render_template('editar_contato.html', contato=contato)  # Renderiza o formulário de edição

@app.route('/marcar_favorito/<int:codigo>')
def marcar_favorito(codigo):
    """
    Rota para marcar um contato como favorito.
    """
    contatos[codigo][4] = True
    return redirect('/')  # Redireciona de volta para a página inicial

@app.route('/desmarcar_favorito/<int:codigo>')
def desmarcar_favorito(codigo):
    """
    Rota para remover um contato da lista de favoritos.
    """
    contatos[codigo][4] = False
    return redirect('/')  # Redireciona de volta para a página inicial

@app.route('/contatos_favoritos')
def contatos_favoritos():
    favoritos = []
    for contato in contatos:
        if contato[4]:
            favoritos.append(contato)
    return render_template('contatos_favoritos.html', favoritos=favoritos)

@app.route('/apagar_contato/<int:codigo>')
def apagar_contato(codigo):
    """
    Rota para apagar um contato da lista.
    """
    del contatos[codigo]
    return redirect('/')  # Redireciona de volta para a página inicial

if __name__ == '__main__':
    app.run(debug=True)  # Executa o aplicativo Flask em modo de depuração se este script for executado diretamente
