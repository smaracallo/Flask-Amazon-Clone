#!/usr/bin/env python3
from flask import Blueprint, render_template

controller = Blueprint('movies', __name__, url_prefix='/movies')
@controller.route('/<string:title>', methods=['GET'])
def lookup(title):
    if title == 'Republic':                     # TODO 2
        return render_template('republic.html') # TODO 2
    else:                                       # TODO 2
        pass                                    # TODO 2
