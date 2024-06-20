import requests
import os
from dotenv import load_dotenv

load_dotenv()

base_url = "https://api.themoviedb.org/3/"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer " + os.getenv("API_KEY")
}

def movie(movie_id):
    url = base_url + "movie/" + str(movie_id) + "?language=en-US"
    response = requests.get(url, headers=headers)
    return response.json()

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
