from psycopg2 import Error
import twitter_auth
import db_connect

def get_follower_count():
  # returns the length of the return from api.follower_ids, which is the same as the number of followers
  return len(api.followers_ids())

def update_follower_count(count):
  # Updates the follower_counts table with the current number of followers and the current timestamp
  connection = db_connect.connect_to_db()
  cursor = connection.cursor()
  try:
    insert_query = '''INSERT INTO follower_counts (COUNT, CREATED_AT) VALUES (%s,%s);'''
    record_to_insert = (count, "now")
    cursor.execute(insert_query, record_to_insert)
    record_count = cursor.rowcount
    if record_count:
      connection.commit()
      print("Updated follower count to ", count)
  except (Exception, Error) as error:
    print("Error updating count: ", error)
  finally:
    db_connect.close_db(connection)


# Authorize
api = twitter_auth.auth()
# Get and update follower count in the table
update_follower_count(get_follower_count())
