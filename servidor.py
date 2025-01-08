#importando o flask
from flask import *
import dao

#criando o servidor flask (back-end)
app = Flask(__name__)
app.secret_key = 'ren876876423@$42'

@app.route('/')
def pageprincipal():
    return render_template('homeifpb.html')

@app.route('/inserirnovadisciplina', methods=['POST'])
def cadastrar_disciplina():
    nome_disc = request.form.get('nomedisciplina')
    print(session['login'])
    disciplinas = session['carrinho']
    disciplinas.append(nome_disc)
    session['carrinho'] = disciplinas
    print(session['carrinho'])
    print('a disciplina foi: ', nome_disc)
    return '<h1>Disciplina inserida com Sucesso!</h1>'
    #tem que fazer uma página html para exibir o retorno

@app.route('/sair')
def fazer_logout():
    session.pop('login')
    return render_template('homeifpb.html')


@app.route('/adicionardisciplina')
def aaa():
    if 'login' in session:
        return render_template('adicionardisciplina.html')
    else:
        return render_template('homeifpb.html')

@app.route('/inseriraluno', methods=['POST'])
def inserir_user():
    matricula = request.form.get('login')
    senha = request.form.get('senha1')
    nome = request.form.get('nome')

    if dao.inserirusuario(matricula, nome, senha):
        msg = 'Usuário cadastrado com sucesso'
    else:
        msg = 'Problemas ao inserir usuário'
    return render_template('homeifpb.html', mensagem=msg)


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')

    resultado = dao.verificarlogin(login, senha)

    if len(resultado) > 0:
        session['login'] = login

        return render_template('homepagealuno.html', user=resultado[0][1])
    else:
        msg = 'Senha ou login incorretos'
        return render_template('homeifpb.html', msglogin=msg)


#iniciando/rodando o servidor
app.run(debug=True)