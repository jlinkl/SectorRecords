from db.run_sql import run_sql
from models.lost_sector import LostSector

def select_all():
    lost_sectors = []

    sql = "SELECT * FROM lost_sectors"
    results = run_sql(sql)

    for row in results:
        lost_sector = LostSector(row['name'], row['id'])
        lost_sectors.append(lost_sector)
    
    return lost_sectors