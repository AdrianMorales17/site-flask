# Importa o flask 

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

name = [ ]

dicionario = {}

# Roda o index.html

@app.route('/', methods=["GET", "POST"])
def home(): 
    if request.method == "POST":
        nome = request.form.get('nome')
        filme = request.form.get('filme')

        adicionar(nome, filme)

        return redirect('/')

    return render_template('index.html')

@app.route('/lista')
def lista():
    return render_template('lista.html', lista=name)

@app.route('/dicionario')
def diciona():
    return render_template('dicionario.html', dados=dicionario)

@app.route('/editar')
def editar():
    return render_template('editar.html')

# Editar o filme no dicionario

@app.route('/editar_filme', methods=["GET","POST"])
def altera_filme():
    if request.method == "POST":

        if not dicionario:
            return redirect(url_for('diciona'))

        nome = request.form.get('nome')
        filme_novo = request.form.get('filme_novo')

        if nome not in dicionario:
            return redirect(url_for('diciona'))

        dicionario[nome] = filme_novo

        return redirect(url_for('diciona'))

    return render_template('editar_filme.html')

# Edita o nome na lista/dicionario

@app.route('/editar_nome', methods=["GET","POST"])
def altera_nome():
    if request.method == "POST":

        if not name:
            return redirect(url_for('diciona'))
        else:
            nome_antigo = request.form.get('nome_antigo')
            nome_novo = request.form.get('nome_novo')

            if nome_antigo not in name:
                return redirect(url_for('lista'))

            editar(nome_antigo, nome_novo) 
                
            return redirect(url_for('diciona'))
    
    return render_template('editar_nome.html')
    
# Exclui os itens da lista/dicionario quando é excluido pela lista

@app.route('/excluir', methods=["GET", "POST"])
def exclui():
    nome = request.form.get('nome')
    origem = request.form.get('origem')

    excluir(nome)

    if origem == "dicionario":
        return redirect(url_for('diciona'))
    elif origem == "lista": 
        return redirect(url_for('lista'))
    


# Cria as funções de tratamento de dados

def adicionar(nome, filme):
    if nome not in name:
        name.append(nome)
    dicionario[nome] = filme

def editar(nome_antigo, nome_novo,):
    if nome_antigo in name:
        index = name.index(nome_antigo)
        name[index] = nome_novo

    # Apaga e edita o nome no dicionario (salva primeiro o filme e dps apaga definitivamente)    
    if nome_antigo in dicionario:
        filme = dicionario[nome_antigo]
        del dicionario[nome_antigo]
        dicionario[nome_novo] = filme

def excluir(nome):
    if nome in name:
        name.remove(nome)
    if nome in dicionario:
        del dicionario[nome]



# Delimita a inicialização do arquivo
if __name__ == '__main__':
    app.run(debug=True)