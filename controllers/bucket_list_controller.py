from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.country import Country
import repositories.country_repository as country_repository
import repositories.sight_repository as sight_repository

bucket_list_blueprint = Blueprint("bucket_list", __name__)

@bucket_list_blueprint.route("/bucket_list")
def all_bucket_list():
    countries = country_repository.select_all()
    sights = sight_repository.select_all()
    return render_template("bucket_list/index.html", all_countries=countries, all_sights=sights)