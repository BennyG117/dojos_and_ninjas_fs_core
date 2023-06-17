from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.ninja_model import Ninja


# route from a-link dojos list @ dojos page to Dojo Show page 
@app.route('/dojoShow/<int:id>')
def show_ninjas():
    return render_template('dojo_show', Dojo = Dojo.ninjas({'id:id'}))