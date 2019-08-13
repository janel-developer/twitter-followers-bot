import db_connect
from psycopg2 import Error

TABLE_SQL = '''CREATE TABLE follower_counts (
      id SERIAL PRIMARY KEY,
      count BIGINT,
      created_at TIMESTAMP); '''


def create_db_table():
    try:
        connection = db_connect.connect_to_db()
        cursor = connection.cursor()
        cursor.execute(TABLE_SQL)
        cursor.close()
        connection.commit()
    except (Exception, Error) as error:
        print(f'Failed to create table: {error}')
    finally:
        db_connect.close_db(connection)


create_db_table()
