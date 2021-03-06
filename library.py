# ad all the imports for application

import sqlite3
from flask import Flask, request, session, g, redirect,\
    url_for, abort, render_template, flash 
from contextlib import closing

#configuration
DATEBASE = '/tmp/flask.db'
DEBUG = True
SECRET_KEY = 'world_in_us'
USERNAME = 'kristina'
PASSWORD = '147258369'

# create application
app = Flask(__name__)
app.config.from_object(__name__)

# download the definitions from the configuration file
# app.config.from_envvar('FLASK_SETTINGS', silent = True)

# connection to the datebase
def connect_db():
    return sqlite3.connect(app.config['DATEBASE'])

# function that initializes the datebase
def init_db():
    with closing(connect_db()) as db:
        with app.open_resource('schema.sql', mode = 'r') as f:
            db.cursor().executescript(f.read())
        db.comit() # confirmation of changes

@app.before_request
def before_request():
    g.db = connect_db()
 
@app.teardown_request
def teardown_request(exception):
    db = getattr(g, 'db',None)
    if db is not None:
        db.close()

# show entries
@app.route('/')
def show_entries():
    cur = g.db.execute('select title, text from entries order by id desc')
    entries = [dict(title = row[0], text = row[1]) for row in cur.fetchall()]
    return render_template('show_entries.html', entries = entries)

# add new entry
@app.route('/add', methods = ['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db.execute('insert into entries (title, text) values (?, ?)',
                 [request.form['title'], request.form['text']])
    g.db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))

# delete one entry
@app.route('/delete/<int:entry_id>')
def delete_entry(entry_id):
    if not session.get('logged_in'):
        abort(401)
#    cur = g.db.execute('select entry_id, title, text from entries order by id desc')
#    entries = [dict(entry_id = row[0], title = row[1], text = row[2]) for row in cur.fetchall()]
    g.db.execute('delete from show_entries where id=' + entry_id)
    g.db.commit()
    flash('Deleted entry %d' % entry_id)
    return redirect( url_for('show_entries'))

# login to the system
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in.')
            return redirect(url_for('show_entries'))
    return render_template('login.html', error = error)

# logout from the system
@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('show_entries'))

if __name__ == '__main__':
    app.run()
