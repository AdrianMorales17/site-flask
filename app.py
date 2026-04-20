# Importa o flask 

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

name = []

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

# Editar o filme no dicionario

@app.route('/editar_filme.html', methods=["GET","POST"])
def altera_filme():
    if request.method == "POST":
        nome = request.form.get('nome')
        filme_novo = request.form.get('filme_novo')

        if nome in dicionario:
            dicionario[nome] = filme_novo

            return redirect('dicionario.html')
        
    return render_template('/editar_filme.html')

# Edita o nome na lista/dicionario

@app.route('/editar_nome', methods=["GET","POST"])
def altera_nome():
    if request.method == "POST":
        nome_antigo = request.form.get('nome_antigo')
        nome_novo = request.form.get('nome_novo')

        editar(nome_antigo, nome_novo) 
            
        return redirect('dicionario.html')
    
    return render_template('/editar_nome.html')
    
# Exclui os itens da lista/dicionario

@app.route('/excluir.html', methods=["GET", "POST"])
def exclui():
    if request.method == "POST":
        nome = request.form.get('nome')

        excluir(nome)

        return redirect('lista.html')
    
    return render_template('')

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