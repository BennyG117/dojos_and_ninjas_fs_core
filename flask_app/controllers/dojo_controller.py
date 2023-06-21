from flask_app import app
from flask import render_template, redirect, request, session, flash, Flask
from flask_app.models.dojo_model import Dojo
from flask_app.models.ninja_model import Ninja



# route home to show all dojos
@app.route('/')
def Home():
    all_dojos = Dojo.get_all()
    return render_template('dojos.html', all_dojos = all_dojos)


# route to show newly added/saved dojo to home page
@app.route('/create/newDojo', methods=['POST'])
def new_dojo():
    print(request.form)
    Dojo.save_dojo(request.form)
    return redirect('/')


# removes a dojo
@app.route('/delete/<int:id>')
def remove(id):
    Dojo.delete({'id':id})

    return redirect('/')



#! must edit once correct join class method is added - -  route from a-link dojos list @ dojos page to Dojo Show page 
@app.route('/dojoShow/<int:id>')
def show_ninjas(id):
    return render_template('dojo_show.html', dojo = Dojo.get_dojo_ninjas({"id":id}))
