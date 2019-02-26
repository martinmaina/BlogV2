from flask import Flask, render_template, request, redirect, url_for, session, flash, g
from functools import wraps
import sqlite3
app = Flask(__name__)

app.secret_key = 'm0Lzixs3m0qy'
app.database = "sample.db"

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first.")
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
    g.db = connect_db()
    cur = g.db.execute('select * from posts')
    posts = []
    for row in cur.fetchall():
        posts.append(dict(title=row[0], description=row[1] ))

       # print(posts)
    #posts =[ dict(title=row[0], description=row[1]) for row in cur.fetchall()]
   
    g.db.close()
    return render_template('index.html', posts=posts)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'user' or request.form['password'] != 'pass':
            error = "Invalid credentials. Please try again"
        else:
            session['logged_in'] = True
            flash('You are logged in')
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    flash('You have been logged out')
    return render_template('logout.html')


def connect_db():
    return sqlite3.connect(app.database)

if __name__ =='__main__':
    app.run(debug=True)