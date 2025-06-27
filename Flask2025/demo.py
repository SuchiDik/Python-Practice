from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

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


# Home Route (Add and Show Todos)
@demo.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("desc")

        if title and desc:
            todo = Todo(title=title, desc=desc)
            db.session.add(todo)
            db.session.commit()

    allTodos = Todo.query.all()
    return render_template("index.html", allTodos=allTodos)


# Delete Route
@demo.route("/delete/<int:sno>")
def delete(sno):
    todo = Todo.query.filter_by(sno=sno).first()
    if todo:
        db.session.delete(todo)
        db.session.commit()
    return redirect(url_for("hello_world"))


# Update Route
@demo.route("/update/<int:sno>", methods=["GET", "POST"])
def update(sno):
    todo = Todo.query.filter_by(sno=sno).first()

    if request.method == "POST":
        title = request.form.get("title")
        desc = request.form.get("desc")

        if title and desc:
            todo.title = title
            todo.desc = desc
            db.session.commit()
            return redirect(url_for("hello_world"))

    return render_template("update.html", todo=todo)


# Debug Route (optional)
@demo.route("/show")
def todos():
    allTodos = Todo.query.all()
    print(allTodos)
    return "Check console for printed todos"


# Run App
if __name__ == "__main__":
    with demo.app_context():
        db.create_all()
demo.run(debug=True)
