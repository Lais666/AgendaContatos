from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista de contatos
contatos = []

@app.route('/')
def index():
    return render_template('index.html', contatos=contatos)

@app.route('/adicionar_contato', methods=['GET', 'POST'])
def adicionar_contato():
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        favorito = 'favorito' in request.form
        contatos.append({'nome': nome, 'telefone': telefone, 'email': email, 'favorito': favorito})
        return redirect('/')
    else:
        return render_template('adicionar_contato.html')

@app.route('/editar_contato/<int:id>', methods=['GET', 'POST'])
def editar_contato(id):
    if request.method == 'POST':
        nome = request.form['nome']
        telefone = request.form['telefone']
        email = request.form['email']
        favorito = 'favorito' in request.form
        contatos[id] = {'nome': nome, 'telefone': telefone, 'email': email, 'favorito': favorito}
        return redirect('/')
    else:
        contato = contatos[id]
        return render_template('editar_contato.html', contato=contato)

@app.route('/marcar_favorito/<int:id>')
def marcar_favorito(id):
    contatos[id]['favorito'] = True
    return redirect('/')

@app.route('/desmarcar_favorito/<int:id>')
def desmarcar_favorito(id):
    contatos[id]['favorito'] = False
    return redirect('/')

@app.route('/contatos_favoritos')
def contatos_favoritos():
    favoritos = [contato for contato in contatos if contato['favorito']]
    return render_template('contatos_favoritos.html', favoritos=favoritos)

@app.route('/apagar_contato/<int:id>')
def apagar_contato(id):
    del contatos[id]
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
