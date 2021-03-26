# from flask import Flask, render_template, jsonify, request, url_for, redirect

# #################################################
# # Flask Setup
# #################################################
# app = Flask(__name__)
# app.static_folder = 'static'

# #################################################
# # Flask Routes
# #################################################
# @app.route("/")
# def welcome():
#     return render_template("index.html")

# ##########  ERROR 404 page not found ##################
# @app.errorhandler(404)
# def page_not_found(error):
#     """Custom 404 page."""
#     return render_template('404.html'), 404


# ##########  ERROR HANDLING ##################
# def error_response(status_code, message=None):
#     payload = {'error': HTTP_STATUS_CODES.get(status_code, 'Unknown error')}
#     if message:
#         payload['message'] = message
#     response = jsonify(payload)
#     response.status_code = status_code
#     return response


# ############# FLASK CLOSING CODE ###################
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, render_template,jsonify
import sqlalchemy
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
import psycopg2

app = Flask(__name__)


@app.route ('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
