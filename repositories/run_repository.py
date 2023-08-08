from db.run_sql import run_sql
from models.run import Run

#return a list of all runs
def select_all():
    runs = []

    sql = "SELECT * FROM runs"
    results = run_sql(sql)

    for row in results:
        run = Run(row['link'], row['season_id'], row['runner_id'], row['lost_sector_id'], row['id'])
        runs.append(run)
    
    return runs

#find a run when using its id
def find(id):
    run = None

    sql = "SELECT * FROM runs WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        run = Run(row['link'], row['season_id'], row['runner_id'], row['lost_sector_id'], row['id'])

    return run

#add a run to the table given its name
def add(run):
    sql = "INSERT INTO runs (link, runner_id, lost_sector_id, season_id) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [run.link, run.runnerid, run.lost_sectorid, run.seasonid]
    results = run_sql(sql, values)
    id = results[0]['id']
    run.id = id
    return run

#change the name of a run
def update(run):
    sql = "UPDATE runs SET (link, runner_id, lost_sector_id, season_id) = (%s, %s, %s, %s) WHERE id = %s"
    values = [run.link, run.runnerid, run.lost_sectorid, run.seasonid, run.id]
    run_sql(sql, values)

#delete a run from the table given its id
def delete(id):
    sql = "DELETE FROM Runs WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    