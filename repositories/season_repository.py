from db.run_sql import run_sql
from models.season import Season

#return a list of all seasons
def select_all():
    seasons = []

    sql = "SELECT * FROM seasons"
    results = run_sql(sql)

    for row in results:
        season = Season(row['name'], row['id'])
        seasons.append(season)
    
    return seasons

#find a season when using its id
def find(id):
    season = None

    sql = "SELECT * FROM seasons WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        season = Season(row['name'], row['id'])

    return season

#add a season to the table given its name
def add(season):
    sql = "INSERT INTO seasons (name) VALUES (%s) RETURNING *"
    values = [season.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    season.id = id
    return season

#change the name of a season
def update(season):
    sql = "UPDATE seasons SET name = %s WHERE id = %s"
    values = [season.name, season.id]
    run_sql(sql, values)

#delete a season from the table given its id
def delete(id):
    sql = "DELETE FROM seasons WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    