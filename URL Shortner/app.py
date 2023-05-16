import os
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import request, redirect, url_for
import pyshorteners

app = Flask(__name__)

##########SQL Alchemy#########################
## Step-1
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] =False

db = SQLAlchemy(app)
Migrate(app, db)

## Step- 2 Create a model

class Shortner(db.Model):
    __tablename__ = "shortner"
    link = db.Column(db.String, primary_key=True)
    shortened_url = db.Column(db.String)

    def __init__(self, link, shortened_url):
        self.link = link
        self.shortened_url = shortened_url

    def __repr__(self):
        return "Link - {} Shortened URL - {}".format(self.link, self.shortened_url)


####################################

@app.route('/history')
def history():
    shortners = Shortner.query.all()
    return render_template("history.html", shortners=shortners)

@app.route('/', methods=['GET', 'POST'])
def homepage():
    if request.method == 'POST':
        original_url = request.form['url']
        s = pyshorteners.Shortener()
        short_url = s.tinyurl.short(original_url)
        shortner = Shortner(link=original_url, shortened_url=short_url)
        db.session.add(shortner)
        db.session.commit()
        return redirect(url_for('history'))
    return render_template("homepage.html")


if __name__ == '__main__':
    app.run(debug = True)
