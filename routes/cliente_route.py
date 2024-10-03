from flask import render_template, Blueprint, request, abort, url_for, redirect
from database.data import conexao

cliente_page = Blueprint("cliente", __name__)


@cliente_page.route("/")
def form_home():
    return render_template("formulario_inicial.html")

@cliente_page.route("/home-page")
def tela_inicial():
    return render_template("tela_inicial.html")

@cliente_page.route("/", methods=["POST"])
def inserir_users():

    # Recebendo dados do formulário form_inicial
    data = request.json

    # Conectando o banco de dados Mysql
    conn = conexao()
    cursor = conn.cursor()

    # Dados Recebidos
    nome = data["user"]
    senha = data["senha"]

    # Comando Sql executado para a verificação de "senha" e "usuario"
    cursor.execute("SELECT idusuarios FROM usuarios WHERE nome_usuarios = %s AND senha_usuarios = %s", (nome, senha))
    user_exists = cursor.fetchone() # Verifica se o usuario existe

    if user_exists:
        conn.close() # Fecha a execução sql
        return redirect(url_for("cliente.tela_inicial"))
        
    else: 
        # Se o usuário não existir, retornar um erro 404
        conn.close() # Fecha a execução sql
        abort(404, description="Usuário ou senha inválidos!") # O abort() interrompe a execução do código e retorna a resposta de erro automaticamente.
