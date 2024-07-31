import psycopg2
from config import load_config
from datetime import datetime
import json


def insert_movie(movie_id, updated_at, json_data):
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
    

if __name__ == '__main__':
    insert_movie(6977, datetime.now(), json.dumps({
  "adult": False,
  "backdrop_path": "/kd9jFTTabg4xJpHDgxY0h8F9BzG.jpg",
  "belongs_to_collection": "",
  "budget": 25000000,
  "genres": [
    {
      "id": 80,
      "name": "Crime"
    },
    {
      "id": 18,
      "name": "Drama"
    },
    {
      "id": 53,
      "name": "Thriller"
    }
  ],
  "homepage": "",
  "id": 6977,
  "imdb_id": "tt0477348",
  "origin_country": [
    "US"
  ],
  "original_language": "en",
  "original_title": "No Country for Old Men",
  "overview": "Llewelyn Moss stumbles upon dead bodies, $2 million and a hoard of heroin in a Texas desert, but methodical killer Anton Chigurh comes looking for it, with local sheriff Ed Tom Bell hot on his trail. The roles of prey and predator blur as the violent pursuit of money and justice collide.",
  "popularity": 53.273,
  "poster_path": "/bj1v6YKF8yHqA489VFfnQvOJpnc.jpg",
  "production_companies": [
    {
      "id": 14,
      "logo_path": "/m6AHu84oZQxvq7n1rsvMNJIAsMu.png",
      "name": "Miramax",
      "origin_country": "US"
    },
    {
      "id": 258,
      "logo_path": "",
      "name": "Scott Rudin Productions",
      "origin_country": "US"
    },
    {
      "id": 2092,
      "logo_path": "/f8s2OKSrnfaCmvCz2LCGxk1WNWO.png",
      "name": "Mike Zoss Productions",
      "origin_country": "US"
    },
    {
      "id": 838,
      "logo_path": "/tcW3UqV46Mdq6GyaS1ydEDocEDF.png",
      "name": "Paramount Vantage",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "2007-06-13",
  "revenue": 171627166,
  "runtime": 122,
  "spoken_languages": [
    {
      "english_name": "English",
      "iso_639_1": "en",
      "name": "English"
    },
    {
      "english_name": "Spanish",
      "iso_639_1": "es",
      "name": "Español"
    }
  ],
  "status": "Released",
  "tagline": "There are no clean getaways.",
  "title": "No Country for Old Men",
  "video": False,
  "vote_average": 7.942,
  "vote_count": 11700
}))