"""
imports render_template to use Flask functionality
imports request from Flask to use request method
imports app and db from taskmanager package
"""
from flask import render_template, request, redirect, url_for
from taskmanager import app, db
from taskmanager.models import Category, Task


@app.route("/")
def home():
    """
    to get the app running, create a basic app route
    using the root-level directory of slash
    this will be used to target the function, 'home'
    the function 'home' will return the rendered-template
    of 'base.html'
    """
    return render_template("tasks.html")


@app.route("/categories")
def categories():
    """
    generate categories template
    """
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    """
    generate add_category template and enable users
    to add a new category to the database
    """
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

