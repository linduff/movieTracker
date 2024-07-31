import psycopg2
from config import load_config
from datetime import datetime
import json
from pgConfig import load_config

def create_movie_details_cache_table(table_name):
    command = """
            CREATE TABLE IF NOT EXISTS movie_details_cache (
                movie_id INT PRIMARY KEY,
                updated_at TIMESTAMP NOT NULL,
                json_data JSONB NOT NULL
            )
            """
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                  cur.execute(command)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_new_movie_into_movie_details_cache_table(movie_id, updated_at, json_data):
    sql = """INSERT INTO movie_details_cache(movie_id, updated_at, json_data)
             VALUES(%s, %s, %s);"""
    
    vendor_id = None

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (movie_id, updated_at, json_data))
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def update_movie_details_cache_table_movie(movie_id, updated_at, json_data):
    sql = """UPDATE movie_details_cache SET updated_at = %s, json_data = %s WHERE movie_id=%s;"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (updated_at, json_data, movie_id))
                
                conn.commit()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def query_movie_details_cache_table_ttl(movie_id):
    sql = """SELECT updated_at FROM movie_details_cache WHERE movie_id=%s;"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, movie_id)
                print(cur.fetchone())

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def query_movie_details_cache_table_json(movie_id):
    sql = """SELECT updated_at FROM movie_details_cache WHERE movie_id=%s;"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, movie_id)
                print(cur.fetchone())

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

if __name__ == '__main__':
    query_movie_details_cache_table_json(6977)
#   insert_new_movie_into_movie_details_cache_table(6977, datetime.now(), json.dumps({
#   "id": 6977,
#   "imdb_id": "tt0477348",
#   "original_language": "en",
#   "original_title": "No Country for Old Men",
#   "popularity": 53.273,
#   "poster_path": "/bj1v6YKF8yHqA489VFfnQvOJpnc.jpg",
#   "status": "Released",
#   "tagline": "There are no clean getaways.",
#   "title": "No Country for Old Men",
#   "video": False,
#   "vote_average": 7.942,
#   "vote_count": 11700
# }))