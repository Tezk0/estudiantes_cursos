from flask import Flask, render_template, redirect, session, request

app = Flask(__name__)

app.secret_key = "llavesecreta v(not necessary but its alright to put it for good measure)"

@app.route("/")
def inicio():
    return redirect("/cursos")

@app.route("/cursos")
def cursos():
    cursos = Curso.get_all