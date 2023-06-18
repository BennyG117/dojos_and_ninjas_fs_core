
from flask_app.config.mysqlconnection import connectToMySQL

class Dojo:
    # use schema name (my db)
    DB = 'dojos_and_ninjas_schema'

    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #method to view a list of all dojos
    @classmethod
    def get_all(cls):
        query = """
        SELECT * 
        FROM dojos;
        """
        results = connectToMySQL(cls.DB).query_db(query)
        # use to check if working...
        print(results)

        dojos = []

        for dojo in results:
            dojos.append( cls(dojo))
        return dojos
    

    #method to save & add new Dojo
    @classmethod
    def save_dojo(cls, data):
        query = """INSERT INTO dojos (name)
        VALUES (%(name)s);
        """

        result = connectToMySQL(cls.DB).query_db(query, data)
        return result
    
    #delete method for dojos
    @classmethod
    def delete(cls, data):
        query = """DELETE FROM dojos 
        WHERE id = %(id)s"""


        result = connectToMySQL(cls.DB).query_db(query, data)
        return result

    #method to get one dojo
    @classmethod
    def get_one(cls, data):
        query = """SELECT * 
        FROM dojos
        WHERE id = %(id)s;"""
        results = connectToMySQL(cls.DB).query_db(query, data)
        singleDojo = cls(results[0])
        
        return singleDojo