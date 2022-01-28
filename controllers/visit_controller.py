from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

visit_blueprint = Blueprint("visited", __name__)

@visit_blueprint.route("/visited")
def all_visited():
    countries = country_repository.select_all()
    sights = sight_repository.select_all()
    return render_template("visited/index.html", all_countries=countries, all_sights=sights)