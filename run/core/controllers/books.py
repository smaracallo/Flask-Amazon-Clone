#!/usr/bin/env python3
from flask import Blueprint, render_template, Flask


controller = Blueprint('books', __name__, url_prefix='/books')
@controller.route('/', methods=['GET'])
def lookup():
    #if title == 'books':                     # TODO 2
    return render_template('books.html') # TODO 2
    # else:                                       # TODO 2
    #     pass                                    # TODO 2
