
class DataAccess(object):
    def __init__(self, connection):
        connection = self.connection
        
    def create_game_instance(self, word, creator):
        query = "INSERT INTO games (hidden_word, creator) VALUES (%s)"
        cursor = self.connection.cursor()
        cursor.execute(query, (word))
        game_id = cursor.fetchone()[0]
        self.connection.commit
        return game_id
    
    def check_for_user(self, username):
        query = "Select * from users where username = %s" #Would typically handle conflicting username in the database with a unique constraint. Just demonstrating I'm thinking about it here.
        cursor = self.connection.cursor()
        cursor.execute(query, (username,))
        results = cursor.fetchone()
        if results is None:
            return None
        else: 
            user_id = results[0]
            return user_id
    
    def create_user(self, username):
        if self.check_for_user() is None:
            query = "INSERT INTO users(username) Values(%s)"
            cursor = self.connection.cursor()
            cursor.execute(query, (username, ))
            user_id = cursor.fetchone()[0]
            self.connection.commit()
            return user_id
    
    def assign_game_to_users(self, usernames, game_id):
        query = "INSERT INTO user_games (user_id, game_id) VALUES(%s, %s)"
        cursor = self.connection.cursor()
        if type(usernames) is list:
            for user in usernames:
                user_id = self.check_for_user(user)
                if user_id  is None:
                    user_id = self.create_user(user)
                cursor.execute(query, (user_id, game_id))
                
        else:
            user_id = self.check_for_user(user)
            if user_id is None:
                user_id = self.create_user(user)
            cursor.execute(query, (user_id, game_id))
        
        self.connection.commit()

    def retrieve_users_games(self, username):
        user_id = self.check_for_user(username=username)
        query= "Select game_id from user_games where user_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (user_id,))
        return cursor.fetchall()
    
    def retrieve_single_game(self, game_id):
        query = "Select * from games where game_id = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (game_id,))
        return cursor.fetchone()
    
    def get_user_id(self, username):
        query = "Select * from users where username = %s"
        cursor = self.connection.cursor()
        cursor.execute(query, (username, ))
        return cursor.fetone()[0]
    
    def update_game_data(self, game_id, user_list, function):
        if function == 'add':
            for user in user_list:
                query = "Insert into user_games (game_id, user_id) values(%s, %s)"
                cursor = self.connection.cursor()
                cursor.execute(query, (game_id, user))
        if function == 'subtract':
            query = "Delete from user_games where user_id in(%s)"
            cursor = self.connection.cursor()
            cursor.execute(query, (tuple(user_list),))



        




    
    