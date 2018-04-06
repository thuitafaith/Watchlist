from flask import render_template,request,redirect,url_for
from app import app
from .request import get_movies,get_movie,search_movie

#views
@app.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    # Getting popular movie
    popular_movies = get_movies('popular')
    upcoming_movies = get_movies('upcoming')
    now_showing_movies = get_movies('now_playing')
    print(popular_movies)
    title = 'Home - Welcome to the best Movie Review Website Online'
    return render_template('index.html', title = title,popular = popular_movies,upcoming = upcoming_movies,now_showing = now_showing_movies)


@app.route('/movie/<int:movie_id>')
def movie(movie_id):
    '''
    View root page function that returns the index page and its data
    '''
    movie = get_movie(movie_id)
    title = f'{movie.title}'
    return render_template('movie.html',id = movie_id, movie = movie)

@app.route('/search/<movie_name>')
def search(movie_name):
    '''
    View function to display the search movie_results
    '''
    movie_name_list = movie_name.split(" ")
    movie_name_format = "+".join(movie_name_list)
    searched_movies = search_movie(movie_name_format)
    title = f'search results for {movie_name}'
    return render_template('search.html',movies = searched_movies)
