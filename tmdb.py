import requests
import os
from dotenv import load_dotenv
import pgCalls

CACHE_TIME_TO_LIVE = 604800 # 1 week in seconds

load_dotenv()

base_url = "https://api.themoviedb.org/3/"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + os.getenv("API_KEY")
}

def movie(movie_id):
    if (datetime.now() - pgCalls.query_movie_details_cache_table_ttl(movie_id)).total_seconds() < CACHE_TIME_TO_LIVE:
        movieJson = pgCalls.query_movie_details_cache_table_json(movie_id)
    else:
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
