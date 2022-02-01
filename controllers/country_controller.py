from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

country_blueprint = Blueprint("countries", __name__)

@country_blueprint.route("/countries")
def countries():
    countries = country_repository.select_all()
    return render_template("countries/index.html", all_countries=countries)

@country_blueprint.route("/countries/new")
def new_country():
    return render_template("countries/new.html")

@country_blueprint.route("/countries", methods=['POST'])
def create_country():
    name = request.form['country_name']
    continent = request.form['continent']
    visited = request.form['visited']
    country = Country(name, continent, visited)
    country_repository.save(country)
    return redirect('/countries')

@country_blueprint.route("/countries/<id>")
def show_country(id):
    country = country_repository.select(id)
    sights = country_repository.sight(country)
    return render_template('countries/show.html', country=country, all_sights=sights)

@country_blueprint.route("/countries/<id>/edit")
def edit_country(id):
    country = country_repository.select(id)
    return render_template('countries/edit.html', country=country)

@country_blueprint.route("/countries/<id>", methods=['POST'])
def update_country(id):
    name = request.form['country_name']
    continent = request.form['continent']
    visited = request.form['visited']

    country = Country(name, continent, visited, id)
    country_repository.update(country)
    return redirect('/countries')

@country_blueprint.route("/countries/<id>/delete", methods=['POST'])
def delete_country(id):
    country_repository.delete(id)
    return redirect('/countries')