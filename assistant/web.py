import os
import  webbrowser


def open_facebook():
    webbrowser.open("https://facebook.com")

def play_misic():
    webbrowser.open("https://www.youtube.com/watch?v=Mesw9H9NQ08")

def open_google():
    webbrowser.open("https://google.com")

def close_browser():
    browserexe1 = "chrome.exe"
    os.system("taskkill /f /im " + browserexe1)
    browserexe2 = "opera.exe"
    os.system("taskkill /f /im " + browserexe2)

def open_cv():
    webbrowser.open("https://whitexgod.github.io/cv-2/")

def open_google_cv():
    webbrowser.open('https://sites.google.com/view/tuhins-portfolio/home?authuser=2')

def open_simon_game():
    webbrowser.open('https://whitexgod.github.io/simon-game/')

def open_my_selling_app():
    webbrowser.open('https://selling-price-predictor.herokuapp.com')

def open_my_movie_sentiment_app():
    webbrowser.open('https://movie-review-sentiment-app.herokuapp.com')

def open_my_movie_recommend_app():
    webbrowser.open('https://movie-recommendation-systemv1.herokuapp.com')

def open_my_github():
    webbrowser.open('https://github.com/whitexgod')

def open_campusx():
    webbrowser.open('http://classroom.campusx.in')

def open_github():
    webbrowser.open('https://github.com')