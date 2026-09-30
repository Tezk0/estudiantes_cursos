from flask import Flask, render_template, redirect, session, request

from curso import Curso

app = Flask(__name__)

app.secret_key = "llavesecreta v(not necessary but its alright to put it for good measure)"

@app.route("/")
def inicio():
    return redirect("/cursos")

@app.route("/cursos")
def cursos():
    cursos = Curso.get_all()

    return render_template("index.html", cursos=cursos)

if __name__ == "__main__":
    app.run(debug=True)