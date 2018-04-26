#!/usr/bin/env python3

from flask import Flask, render_template, request
import sqlite3 as sql

from core.controllers.books import controller as books
from core.controllers.electronics import controller as electronics
from core.controllers.movies import controller as movies
from core.controllers.home import controller as home
from core.controllers.food import controller as food
from core.controllers.beauty import controller as beauty
from core.controllers.toys import controller as toys
from core.controllers.clothing import controller as clothing
from core.controllers.handmade import controller as handmade
from core.controllers.sports import controller as sports
from core.controllers.automotive import controller as automotive


omnibus = Flask(__name__)
omnibus.register_blueprint(books)
omnibus.register_blueprint(electronics)
omnibus.register_blueprint(movies)
omnibus.register_blueprint(home)
omnibus.register_blueprint(food)
omnibus.register_blueprint(beauty)
omnibus.register_blueprint(toys)
omnibus.register_blueprint(clothing)
omnibus.register_blueprint(handmade)
omnibus.register_blueprint(sports)
omnibus.register_blueprint(automotive)

@omnibus.route('/',methods = ['GET','POST'])
def index():
    return render_template('register.html')

