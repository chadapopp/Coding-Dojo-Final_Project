from flask_app.config.mysqlconnection import connectToMySQL


class User:
    DB = "rv_rentals_schema"
    def __init__(self, user_dict):
        self.id = user_dict["id"]
        self.first_name = user_dict['first_name']
        self.last_name = user_dict['last_name']
        self.email = user_dict["email"]
        self.password = user_dict["password"]
        self.created_at = user_dict["created_at"]
        self.updated_at = user_dict["updated_at"]

        self.files = []

    @classmethod
    def get_by_email(cls, data):
        query = "SELECT * FROM users WHERE email=%(email)s"
        result = connectToMySQL(cls.DB).query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    @classmethod
    def get_by_id(cls,user_id):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        data = {'id': user_id}
        results = connectToMySQL(cls.DB).query_db(query,data)
        return cls(results[0])


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users"
        result = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user_dict in result:
            users.append(cls(user_dict))

        return users
    
    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s)"
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
