#importando o flask
from flask import *
import dao

#criando o servidor flask (back-end)
app = Flask(__name__)
app.secret_key = 'sdfhsdjfg345@$42'


#from rotas.usuarios import  usuarios_bp

#app.register_blueprint(usuarios_bp, url_prefix="/usuariosx")


@app.route('/')
def pageprincipal():
    return render_template('homeifpb.html')


@app.route('/sair')
def fazer_logout():
    session.pop('login')
    return render_template('homeifpb.html')


@app.route('/adicionardisciplina', methods=['POST', 'GET'])
def inserir_disciplina():

    if request.method == 'POST':
        nome_disciplina = request.form.get('nomedisciplina')
        login_aluno = session['login']
        if dao.inserir_disciplina(nome_disciplina, login_aluno):
            return '<h1>disciplina inserida com sucesso</h1>'
        else:
            return '<h1>Problema ao inserir disciplina</h1>'

    else:
        return render_template('adicionardisciplina.html')


@app.route('/listardisciplinas')
def listar_disciplinas():
    disciplinas = dao.listar_disciplinas(session['login'])

    return render_template('listardisciplinas.html', lista=disciplinas)


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

#-----------------------API métodos

@app.route('/listarusuarios')
def listar_usuarios():
    listaUsuarios = dao.listarpessoas()

    #jsonify converte a lista de itens para o formato JSON
    return jsonify(listaUsuarios), 200


if __name__ == '__main__':
    app.run(debug=True)