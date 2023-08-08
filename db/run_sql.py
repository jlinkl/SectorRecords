import psycopg2
import psycopg2.extras as ext

def run_sql(sql, values = None):
    conn = None
    results = []

    try:
        conn=psycopg2.connect("dbname='sector_records'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        cur.execute(sql, values)
        conn.commit()
        results = cur.fetchall()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return results  
    
def reset_tables():
    conn = None
    results = []

    fd = open ('db/sector_records.sql', 'r')
    sqlFile = fd.read()
    fd.close()

    sqlCommands = sqlFile.split(';')

    try:
        conn=psycopg2.connect("dbname='sector_records'")
        cur = conn.cursor(cursor_factory=ext.DictCursor)
        for command in sqlCommands:
            cur.execute(command)
            conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
        return results 