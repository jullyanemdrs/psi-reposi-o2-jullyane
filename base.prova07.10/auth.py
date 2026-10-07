from flask import Blueprint, flash, redirect, render_template, request, session, url_for
from werkzeug.security import check_password_hash, generate_password_hash

import database


auth_bp = Blueprint("auth", __name__)

# - a rota /registro;
@auth_bp.route("/registro", methods=["GET", "POST"])
def registro():
    if request.method == "POST":
        nome = request.form.get("nome", "")
        email = request.form.get("email", "")
        senha = request.form.get("senha", "")

        if not nome or not email or not senha:
            flash("Campos obrigatórios.")
            return redirect(url_for("auth.registro"))

        if database.buscar_usuario_por_email(email):
            flash("E-mail já cadastrado.")
            return redirect(url_for("auth.registro"))

        senha_hash = generate_password_hash(senha)
        database.criar_usuario(nome, email, senha_hash)
        flash("Cadastro realizado com sucesso.")
        return redirect(url_for("auth.login"))

    return render_template("registro.html")

# - a rota /login;
@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        flash("Implemente o login com session.")
        return redirect(url_for("auth.login"))

    if "usuario_id" in session:
        flash("Você já está logado.")
        return redirect(url_for("index"))

    if request.method == "POST":
        email = request.form.get("email", "")
        senha = request.form.get("senha", "")

        usuario = database.buscar_usuario_por_email(email)
        if usuario and check_password_hash(usuario["senha"], senha):
            session["usuario_id"] = usuario["id"]
            session["usuario_nome"] = usuario["nome"]
            flash("Login realizado com sucesso.")
            return redirect(url_for("index"))
        else:
            flash("E-mail ou senha inválidos.")
            return redirect(url_for("auth.login"))
    




    return render_template("login.html")

# - a rota /logout.

@auth_bp.route("/logout")
def logout():
    flash("Implemente o logout com session.")
    return redirect(url_for("index"))

# Complete este arquivo durante a avaliação.
#
# O Blueprint já está criado, mas nenhuma rota foi vinculada ainda.
# Implemente aqui:
#


