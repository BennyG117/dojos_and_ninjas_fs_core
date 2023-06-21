
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja_model

class Dojo:
    # use schema name (my db)
    DB = 'dojos_and_ninjas_schema'

    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.all_ninjas = []

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
    


    #classmethod to join the one to many so we can use get_ninjas
    #need to use LEFT JOIN so it returns dojos with no ninjas as well*
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = """SELECT * FROM dojos 
        LEFT JOIN ninjas 
        ON ninjas.dojo_id = dojos.id
        WHERE dojos.id = %(id)s;
        """
        #ref database name for connect to my sql below (aka DB) - class name. db name  -- if within static and a method inside, then add to 
        results = connectToMySQL(cls.DB).query_db(query, data)

        dojo = cls(results[0])
        for joined_row_from_db in results:
        
        #if it has the same name then specify the second table you join like: ninjas.id then unique one are just the names
            ninjaData = {
                "id" : joined_row_from_db["ninjas.id"],
                "first_name" : joined_row_from_db["first_name"],
                "last_name" : joined_row_from_db["last_name"],
                "age" : joined_row_from_db["age"],
                "created_at" : joined_row_from_db["ninjas.created_at"],
                "updated_at" : joined_row_from_db["ninjas.updated_at"],
                "dojo_id" : joined_row_from_db["dojo_id"]

            }
            dojo.all_ninjas.append(ninja_model.Ninja(ninjaData))
        return dojo