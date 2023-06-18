from flask_app.config.mysqlconnection import connectToMySQL

class Ninja:
    # use schema name (my db)
    DB = 'dojos_and_ninjas_schema'

    def __init__(self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    

    #method to save submitted new ninja data by adding it to our DB
    @classmethod
    def save(cls, data):
        query = """INSERT INTO ninjas (first_name, last_name, age, dojo_id)
                VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s );"""
        
        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    # method to get all ninjas from specific dojo
    @classmethod
    def get_ninjas(cls, data):
        query = """
        SELECT *
        FROM ninjas
        WHERE dojo_id = %(id)s;
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
    
        ninjas = []

        for ninja in result:
            ninjas.append( cls(ninja))
        return ninjas
