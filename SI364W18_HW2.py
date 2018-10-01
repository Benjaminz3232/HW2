## SI 364
## Fall 2018
## HW 2
## Benjamin Zeffer YEEEEEEEEET

## This homework has 3 parts, all of which should be completed inside
## this file (and a little bit inside the /templates directory).

## Add view functions and any other necessary code to this Flask
## application code below so that the routes described in the README
## exist and render the templates they are supposed to (all templates
## provided are inside the templates/ directory, where they should
## stay).

## As part of the homework, you may also need to add templates
## (new .html files) to the templates directory.

#############################
##### IMPORT STATEMENTS #####
#############################
from flask import Flask, request, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, ValidationError
from wtforms.validators import Required
import requests
import json

#####################
##### APP SETUP #####
#####################

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hardtoguessstring'

####################
###### FORMS #######
####################

class AlbumEntryForm(FlaskForm):
    name_of_album = StringField('Enter the name of an album:', validators=[Required()])
    options = RadioField('How much do you enjoy this album? (1 lowest, 3 highest)',choices=[('1','1'),('2','2'),('3','3')],validators=[Required()])
    submit = SubmitField('Submit')

####################
###### ROUTES ######
####################

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/user/<name>')
def hello_user(name):
    return '<h1>Hello {0}<h1>'.format(name)

####################
#### MY ROUTES ##### Benjamin Zeffer yeet yeet yeet YEEEEEEEEEEEEEET
####################

@app.route('/artistform')
def artist_form():
    return render_template('artistform.html')

@app.route('/artistinfo', methods=['GET', 'POST'])
def artist_info():
    base_url = "https://itunes.apple.com/search?"
    
    artist = request.args.get('artist',"")
    param_dict = {'term': artist, 'entity' : 'musicTrack'}

    r = requests.get(base_url, params = param_dict)
    response = json.loads(r.text)['results']

    return render_template('artist_info.html', objects=response)

@app.route('/artistlinks')
def artist_links():
    return render_template('artist_links.html')

@app.route('/specific/song/<artist_name>', methods=['GET', 'POST'])
def specific_artist(artist_name):
    param_dict = {'term': artist_name, 'entity':'musicTrack'}
    base_url = "https://itunes.apple.com/search?"

    r = requests.get(base_url, params=param_dict)
    response = r.json()['results']

    return render_template('specific_artist.html', results=response)

@app.route('/album_entry')
def album_entry():
    simpleForm = AlbumEntryForm()
    return render_template('album_entry.html', form=simpleForm)

@app.route('/album_result', methods=['GET', 'POST'])
def album_result():
    form = AlbumEntryForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        name_of_album = form.name_of_album
        options = form.options.data

        return render_template('album_data.html', name_of_album=name_of_album, options=options)

    flash('All fields are required!')

    return redirect(url_for('/album_entry'))

## Benjamin Zeffer yeet yeet yeet

if __name__ == '__main__':
    app.run(use_reloader=True,debug=True)
