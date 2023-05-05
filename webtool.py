from flask import Flask
from flask import session
from wordList import word_list
from flask import request
from dataAccess import DataAccess
from game import Game

import os
import psycopg2
import random


DATABASE = os.environ["DATABASE"]
USER = os.environ["PG_USER"]
PASSWORD = os.environ["PG_PASSWORD"]
URL = os.environ['PG_URL']
PORT = os.environ["PG_PORT"]

connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=URL, port=PORT, sslmode='allow')
data = DataAccess(connection=connection)

SECRET_KEY = os.environ["SECRET_KEY"]
app = Flask(__name__)

@app.route("/")
def server_test():
    return "confirmed"

@app.route("/createGameInstance", methods=['POST'])
def create_game_instance():
    word = random.choice(word_list)
    user = request.form["user"]
    usernames = request.form['usernames'] #can accept a list of users or a single user. Creator first if a list
    session['usernames'] = usernames
    usernames.append(user)

    game_id = data.create_game_instance(word=word, creator=user)
    data.assign_game_to_users(usernames, game_id=game_id)

@app.route("/retrieveAllGameInstances", methods=["GET"])
def retrieve_all_game_instances():
    username = request.args.get('username')
    data.retrieve_users_games(username=username)

@app.route("/retrieveGameState", methods=["GET"])
def retrieve_single_game_state():
    game = request.args.get('game_id')
    single_game_state = data.retrieve_single_game(game_id=game)
    return single_game_state

@app.route("/updateGame", methods=["POST"])
def update_games():
    username = session['user']
    game = request.args.get('game_id')
    user_list = request.args.get('userlist')
    function = request.args.get('function')
    game_data = data.retrieve_single_game(game)
    creator = game_data[2]
    userid = data.get_user_id(username)
    if userid == creator:
        data.update_game_data(game_id=game,user_list=user_list, function=function)

@app.route('ventureGuess', methods= ['POST'])
def venture_guess():
    username=request.args.get('username')
    game = data.retrieve_single_game(username)
    hidden_word = game[1]
    guess = request.args.get('guess')
    data.guess(winner=hidden_word, guess=guess)

       



