import requests
import os
from dotenv import load_dotenv
from datetime import datetime
import pgCalls

print("starting tmdb")
CACHE_TIME_TO_LIVE = 604800 # 1 week in seconds

base_url = "https://api.themoviedb.org/3/"

load_dotenv()

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + os.getenv("API_KEY")
}

def movie(movie_id):
    print("Getting data for movie " + str(movie_id))
    if pgCalls.query_movie_details_cache_table_json(movie_id) == None:
        url = base_url + "movie/" + str(movie_id) + "?language=en-US"
        movieJson = pgCalls.insert_new_movie_into_movie_details_cache_table(movie_id, datetime.now(), requests.get(url, headers=headers).json())
    elif (datetime.now() - pgCalls.query_movie_details_cache_table_ttl(movie_id)).total_seconds() < CACHE_TIME_TO_LIVE:
        print("Movie is fresh and being retrieved from cache")
        movieJson = pgCalls.query_movie_details_cache_table_json(movie_id)
    else:
        print("Movie is stale and being fetched and updated in the cache.")
        url = base_url + "movie/" + str(movie_id) + "?language=en-US"
        response = requests.get(url, headers=headers)
        pgCalls.update_movie_details_cache_table_movie(movie_id, datetime.now(), response.json())
        movieJson = response.json()
    return movieJson

def search_movies(query, page=1):
    url = base_url + "search/movie?query=" + query + "&include_adult=false&language=en-US&page=" + str(page)
    response = requests.get(url, headers=headers)
    return response.json()

def popular_movies(page=1):
    url = base_url + "movie/popular?language=en-US&page=" + str(page)
    response = requests.get(url, headers=headers)
    return response.json()

def upcoming_movies(page=1):
    url = base_url + "movie/upcoming?language=en-US&page=" + str(page)
    response = requests.get(url, headers=headers)
    return response.json()

def now_playing_movies(page=1):
    url = base_url + "movie/now_playing?language=en-US&page=" + str(page)
    response = requests.get(url, headers=headers)
    return response.json()

def top_rated_movies(page=1):
    url = base_url + "movie/top_rated?language=en-US&page=" + str(page)
    response = requests.get(url, headers=headers)
    return response.json()

# if __name__ == '__main__':
    

# print(popular_movies())