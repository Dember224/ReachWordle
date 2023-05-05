CREATE TABLE games (
    game_id serial primary key,
    hidden_word char(10),
    creator int references user(user_id),
    guess_1 char(10),
    guess_2 char(10),
    guess_3 char(10),
    guess_4 char(10),
    guess_5 char(10),
    guess_5 char(10)
);

CREATE TABLE user(
    user_id serial primary key,
    username
);

CREATE TABLE user_games(
    user_game_id serial primary key, 
    user_id int references user(user_id),
    game_id int references game(game_id)
)