from flask import render_template, Blueprint, request, jsonify, redirect
from database.data import conexao

create_page = Blueprint("criacao", __name__)

@create_page.route("/")
def form_criar_user():
    return render_template("formulario_criacao.html")

@create_page.route("/create", methods=["POST"])
def criar_users():

    data = request.json
    conn = conexao()
    cursor = conn.cursor()

    nome = data["user"]
    senha = data["senha"]

    cursor.execute("SELECT idusuarios FROM usuarios WHERE nome_usuarios = %s", (nome,))
    user_exists = cursor.fetchone()

    if user_exists:
        conn.close() # Fecha a execução sql
        return {"mensagem": "Usuario já existente!"}
    else: 
        comando = f'INSERT INTO usuarios (nome_usuarios, senha_usuarios) VALUES ("{nome}", {senha})'
        message = "Usuario Criado!"
        cursor.execute(comando) 
        conn.commit()   
        conn.close()
   
    return jsonify({"message": message})