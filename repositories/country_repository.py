from db.run_sql import run_sql

from models.country import Country
from models.sight import Sight


def save(country):
    sql = "INSERT INTO countries (country_name, continent, visited) VALUES (%s, %s, %s) RETURNING *"
    values = [country.country_name, country.continent, country.visited]
    results = run_sql(sql, values)
    id = results[0]['id']
    country.id = id
    return country


# def select_all():
#     countries = []

#     sql = "SELECT * FROM countries"
#     results = run_sql(sql)

#     for row in results:
#         country = Country(row['country_name'], row['continent'], row['visited'], row['id'])
#         countries.append(country)
#     return countries


# def select(id):
#     country = None
#     sql = "SELECT * FROM countries WHERE id = %s"
#     values = [id]
#     result = run_sql(sql, values)[0]

#     if result is not None:
#         country = Country(result['country_name'], result['continent'], result['visited'], result['id'])
#     return country


# def delete_all():
#     sql = "DELETE FROM countries"
#     run_sql(sql)


# def delete(id):
#     sql = "DELETE FROM countries WHERE id = %s"
#     values = [id]
#     run_sql(sql, values)


# def update(country):
#     sql = "UPDATE countries SET (country_name, continent, visited) = (%s, %s, %s) WHERE id = %s"
#     values = [country.country_name, country.continent, country.visited, country.id]
#     run_sql(sql, values)


# def cities(country):
#     sights = []

#     sql = "SELECT * FROM sights WHERE country_id = %s"
#     values = [country.id]
#     results = run_sql(sql, values)

#     for row in results:
#         sight = Sight(row['sight_name'], country, row['visited'], row['id'])
#         sights.append(sight)
#     return sights