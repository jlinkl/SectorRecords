from db.run_sql import run_sql
from models.runner import Runner

#return a list of all runners
def select_all():
    runners = []

    sql = "SELECT * FROM runners"
    results = run_sql(sql)

    for row in results:
        runner = Runner(row['name'], row['id'])
        runners.append(runner)
    
    return runners

#find a runner when using their id
def find(id):
    runner = None

    sql = "SELECT * FROM runners WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        runner = Runner(row['name'], row['id'])

    return runner

#add a runner to the table given their name
def add(runner):
    sql = "INSERT INTO runners (name) VALUES (%s) RETURNING *"
    values = [runner.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    runner.id = id
    return runner

#change the name of a runner
def update(runner):
    sql = "UPDATE runners SET name = %s WHERE id = %s"
    values = [runner.name, runner.id]
    run_sql(sql, values)

#delete a runner from the table given their id
def delete(id):
    sql = "DELETE FROM runners WHERE id = %s"
    values = [id]
    run_sql(sql, values)
    