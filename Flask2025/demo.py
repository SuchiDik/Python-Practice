import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

demo = Flask(__name__)
demo.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
demo.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(demo)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"{self.sno} - {self.title}"


@demo.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("desc")
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()

    allTodos = Todo.query.all()
    return render_template("index.html", allTodos=allTodos)


@demo.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.get_or_404(sno)
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@demo.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    todo = Todo.query.get_or_404(sno)
    if request.method == "POST":
        todo.title = request.form.get("title")
        todo.desc = request.form.get("desc")
        db.session.commit()
        return redirect("/")
    return render_template("update.html", todo=todo)


if __name__ == "__main__":
    with demo.app_context():
        db.create_all()
    port = int(os.environ.get("PORT", 5000))
demo.run(host="0.0.0.0", port=port, debug=True)
