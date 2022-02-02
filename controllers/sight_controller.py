from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.sight import Sight
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

sight_blueprint = Blueprint("sights", __name__)

@sight_blueprint.route("/sights")
def sights():
    sights = sight_repository.select_all()
    return render_template("sights/index.html", all_sights = sights)

@sight_blueprint.route("/sights/new", methods=['GET'])
def new_sight():
    countries = country_repository.select_all()
    return render_template("sights/new.html", all_countries = countries)

@sight_blueprint.route("/sights",  methods=['POST'])
def create_sight():
    name = request.form['sight_name']
    country_id = request.form['country_id']
    description = request.form['description']
    visited = request.form['visited']
    country = country_repository.select(country_id)
    sight = Sight(name, country, description, visited)
    sight_repository.save(sight)
    return redirect('/sights')

@sight_blueprint.route("/sights/<id>")
def show_sight(id):
    sight = sight_repository.select(id)
    return render_template('sights/show.html', sight=sight)

@sight_blueprint.route("/sights/<id>/edit", methods=['GET'])
def edit_sight(id):
    sight = sight_repository.select(id)
    countries = country_repository.select_all()
    return render_template('sights/edit.html', sight = sight, all_countries = countries)

@sight_blueprint.route("/sights/<id>", methods=['POST'])
def update_sight(id):
    sight_name = request.form['sight_name']
    # country_id = request.form['country_id']
    country = country_repository.select(request.form['country_id'])
    description = request.form['description']
    visited = request.form['visited']
    sight = Sight(sight_name, country, description, visited)
    sight_repository.update(sight)
    return redirect('/sights')

@sight_blueprint.route("/sights/<id>/delete", methods=['POST'])
def delete_sights(id):
    sight_repository.delete(id)
    return redirect('/sights')