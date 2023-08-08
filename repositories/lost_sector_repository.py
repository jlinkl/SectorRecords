from db.run_sql import run_sql
from models.lost_sector import LostSector

#return a list of all lost sectors
def select_all():
    lost_sectors = []

    sql = "SELECT * FROM lost_sectors"
    results = run_sql(sql)

    for row in results:
        lost_sector = LostSector(row['name'], row['id'])
        lost_sectors.append(lost_sector)
    
    return lost_sectors

#find a lost sector when using its id
def find(id):
    lostsector = None

    sql = "SELECT * FROM lost_sectors WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)

    if result:
        row = result[0]
        lostsector = LostSector(row['name'], row['id'])

    return lostsector

#add a lost sector to the table given its name
def add(lost_sector):
    sql = "INSERT INTO lost_sectors (name) VALUES (%s) RETURNING *"
    values = [lost_sector.name]
    results = run_sql(sql, values)
    id = results[0]['id']
    lost_sector.id = id
    return lost_sector
    