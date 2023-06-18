from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.ninja_model import Ninja
from flask_app.models.dojo_model import Dojo


# route for add a new Ninja (calling a dojo class)
@app.route('/newNinja/add')
def viewNinjaForm():
    dojos = Dojo.get_all()
    return render_template('new_ninja.html', all_dojos = dojos)

# route for adding a new ninja, then takes us to Dojo show for that individual dojo
@app.route('/newNinja/save', methods=['POST'])
def saveNinja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/')