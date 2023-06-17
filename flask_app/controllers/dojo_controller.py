from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.dojo_model import Dojo

#! can we use this for create_dojo method as well, so it shows the updated dojo list after adding a new dojo 
# route home
@app.route('/')
def Home():
    all_dojos = Dojo.get_all()
    return render_template('dojos.html', all_dojos = all_dojos)



 