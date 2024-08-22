import psycopg2
from datetime import datetime
import json
from pgConfig import load_config

print("starting pgCalls")

create_movie_log_table = """
CREATE TABLE IF NOT EXISTS movie_log (
	log_id SERIAL PRIMARY KEY,
	movie_id INT,
	created_at TIMESTAMP NOT NULL,
	title TEXT,
	rating INT,
	comments TEXT,
	watch_date TEXT,
	tage TEXT[]
)
"""

create_movie_details_cache_table = """
CREATE TABLE IF NOT EXISTS movie_details_cache (
	movie_id INT PRIMARY KEY,
	updated_at TIMESTAMP NOT NULL,
	backdrop_path TEXT,
	belongs_to_collection INT[],
	budget INT
	genres INT[],
	homepage TEXT,
	imdb_id TEXT,
	origin_country TEXT[],
	original_language TEXT,
	original_title TEXT,
	overview TEXT,
	popularity FLOAT4,
	poster_path TEXT,
	production_companies INT[],
	production_countries TEXT[],
	release_date TEXT,
	revenue INT,
	runtime INT,
	spoken_languages TEXT[],
	status TEXT,
	tagline TEXT,
	title TEXT
)
"""

create_movie_collections_table = """
CREATE TABLE IF NOT EXISTS movie_collections (
	id INT PRIMARY KEY,
	name TEXT,
	poster_path TEXT,
	backdrop_path TEXT
)
"""

create_movie_genres_table = """
CREATE TABLE IF NOT EXISTS movie_genres (
	id INT PRIMARY KEY,
	name TEXT,
)
"""

create_movie_origin_countries_table = """
CREATE TABLE IF NOT EXISTS movie_origin_countries (
	id SERIAL PRIMARY KEY,
	country_name TEXT,
)
"""

create_movie_production_companies_table = """
CREATE TABLE IF NOT EXISTS movie_production_companies (
	id INT PRIMARY KEY,
	logo_path TEXT,
	name TEXT,
	origin_country TEXT
)
"""

create_movie_production_countries_table = """
CREATE TABLE IF NOT EXISTS movie_production_countries (
	id SERIAL PRIMARY KEY,
	iso_3166_1 TEXT,
	name TEXT
)
"""

create_movie_movie_spoken_languages_table = """
CREATE TABLE IF NOT EXISTS movie_spoken_languages (
	id SERIAL PRIMARY KEY,
	english_name TEXT,
	iso_639_1 TEXT,
	name TEXT
)
"""

def create_movie_details_cache_table(table_name):
    config = load_config()

    try:
        with psycopg2.connect(**config) as conn:
            with conn.cursor() as cur:
                  cur.execute(create_movie_details_cache_table)
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)

def insert_new_movie_into_movie_details_cache_table(movie_id, updated_at, json_data):
    sql = """INSERT INTO movie_details_cache(movie_id, updated_at, json_data) VALUES(%s, %s, %s);"""

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
                cur.execute(sql, (movie_id,))
                return cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

def query_movie_details_cache_table_json(movie_id):
    sql = """SELECT json_data FROM movie_details_cache WHERE movie_id=%s;"""

    config = load_config()

    try:
        with  psycopg2.connect(**config) as conn:
            with  conn.cursor() as cur:
                cur.execute(sql, (movie_id,))
                return cur.fetchone()

    except (Exception, psycopg2.DatabaseError) as error:
        print(error)

