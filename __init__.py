from flask import Flask, render_template, redirect, \
    url_for, request, session, flash, g, make_response, send_file
from flask.ext.login import LoginManager, login_user, logout_user, current_user, login_required
from functools import wraps
import MySQLdb
from MySQLdb import escape_string as thwart
import json
import datetime
from datetime import datetime,timedelta
from time import mktime
import os
import time
import urllib2
from wtforms import Form, BooleanField, TextField, PasswordField, validators
from passlib.hash import sha256_crypt
from dbconnect import connection
import gc
# Dictates urls and linkage
from content_management import Content
import smtplib
from flask_mail import Mail, Message



app = Flask(__name__)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.gmail.com',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'your@gmail.com',
	MAIL_PASSWORD = 'yourpassword'
	)
mail = Mail(app)


# list of topics by {TOPIC:["TITLE", "URL"]}
TOPIC_DICT = Content()

class User:
    def username(self):
        try:
            return str(session['username'])
        except:
            return("guest")

user = User()

def userinformation():
    try:
        client_name = (session['username'])
        guest = False
    except:
        guest = True
        client_name = "Guest"
        
    if not guest:
        try:
            c,conn = connection()
            c.execute("SELECT * FROM users WHERE username = (%s)",
                    (thwart(client_name)))
            data = c.fetchone()
            settings = data[4]
            tracking = data[5]
            rank = data[6]
        except Exception, e:
            pass

    else:
        settings = [0,0]
        tracking = [0,0]
        rank = [0,0]
        
    return client_name, settings, tracking, rank

def update_user_tracking():
    try:
        completed = str(request.args['completed'])
        if completed in str(TOPIC_DICT.values()):
            client_name, settings, tracking, rank = userinformation()
            if tracking == None:
                tracking = completed
            else:
                if completed not in tracking:
                    tracking = tracking+","+completed
            
            c,conn = connection()
            c.execute("UPDATE users SET tracking = %s WHERE username = %s",
                    (thwart(tracking),thwart(client_name)))
            conn.commit()
            c.close()
            conn.close()
            client_name, settings, tracking, rank = userinformation()

        else:
            pass

            
    except Exception, e:
        pass
        #flash(str(e))


class RegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')
    accept_tos = BooleanField('I accept the <a href="/about/tos" target="blank">Terms of Service</a> and <a href="/about/privacy-policy" target="blank">Privacy Notice</a> (updated Jan 22, 2015)', [validators.Required()])
    

## LIVE VERSION ####
@app.route('/robots.txt/')
def robots():
    return("User-agent: *\nDisallow: /register/\nDisallow: /login/\nDisallow: /donation-success/")


@app.route('/return-files/')
def return_files_tut():
    try:
        return send_file('/var/www/PythonProgramming/PythonProgramming/static/images/python.jpg', attachment_filename='python.jpg')
        #return send_file('/var/www/PythonProgramming/PythonProgramming/static/ohhey.pdf', attachment_filename='ohhey.pdf')
    except Exception as e:
        return str(e)

@app.route('/file-downloads/')
def file_downloads():
    try:
        return render_template('downloads.html')
    except Exception as e:
        return str(e)


###### DEV VERSION #####
##@app.route('/robots.txt/')
##def robots():
##    return("User-agent: *\nDisallow: /")
##

@app.route('/sitemap.xml', methods=['GET'])
def sitemap():
    try:
      """Generate sitemap.xml. Makes a list of urls and date modified."""
      pages=[]
      ten_days_ago=(datetime.now() - timedelta(days=7)).date().isoformat()
      # static pages
      for rule in app.url_map.iter_rules():
          if "GET" in rule.methods and len(rule.arguments)==0:
              pages.append(
                           ["http://pythonprogramming.net"+str(rule.rule),ten_days_ago]
                           )

      sitemap_xml = render_template('sitemap_template.xml', pages=pages)
      response= make_response(sitemap_xml)
      response.headers["Content-Type"] = "application/xml"    
    
      return response
    except Exception as e:
        return(str(e))


def index(chartID = 'chart_ID', chart_type = 'bar', chart_height = 350):
	chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
	series = [{"name": 'Label1', "data": [1,2,3]}, {"name": 'Label2', "data": [4, 5, 6]}]
	title = {"text": 'My Title'}
	xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
	yAxis = {"title": {"text": 'yAxis Label'}}
	return render_template('index.html', chartID=chartID, chart=chart, series=series, title=title, xAxis=xAxis, yAxis=yAxis)
 


    
@app.route('/', methods=['GET', 'POST'])
def main():
    form = RegistrationForm(request.form)
    try:
        c,conn = connection()
        error = None
        if request.method == 'POST':
            try:
                data = c.execute("SELECT * FROM users WHERE username = (%s)",
                        thwart(request.form['username']))
                data = c.fetchone()[2]

                if sha256_crypt.verify(request.form['password'], data):
                    session['logged_in'] = True
                    session['username'] = request.form['username']
                    flash('You are now logged in.')
                    return redirect(url_for('dashboard'))
            except Exception, e:
                flash("What are you doing?")


            try:
                
                if request.method == 'POST' and form.validate():

                    username = form.username.data
                    email = form.email.data

                    password = sha256_crypt.encrypt((str(form.password.data)))
                    c,conn = connection()

                    x = c.execute("SELECT * FROM users WHERE username = (%s)",
                        (thwart(username)))

                    if int(x) > 0:
                        flash("That username is already taken, please choose another")
                        return render_template('register.html', form=form)

                    else:
                        c.execute("INSERT INTO users (username, password, email) VALUES (%s, %s, %s)",
                            (thwart(username), thwart(password), thwart(email)))
                        conn.commit()
                        flash('Thanks for registering')
                        c.close()
                        conn.close()
                        gc.collect()
                        session['logged_in'] = True
                        session['username'] = username
                        return redirect(url_for('dashboard'))

            except Exception as e:
                return(str(e))
  
            else:
                flash('Invalid credentials. Try again')
        gc.collect()
        return render_template("main.html", error=error, form=form, page_type = "main")
    except Exception, e:
        return(str(e))


@app.route('/jinjaman/')
def jinjaman():
    try:
        gc.collect()
        data = [15, '15', 'Python is good','Python, Java, php, SQL, C++','<p><strong>Hey there!</strong></p>']
        return render_template("jinja-templating.html", data = data)
    except Exception, e:
        return(str(e))
 


@app.route('/include_example/')
def include_example():
    try:
        replies = {'Jack':'Cool post',
                   'Jane':'+1',
                   'Erika':'Most definitely',
                   'Bob':'wow',
                   'Carl':'amazing!',}
        return render_template("includes_tutorial.html", replies = replies)
    except Exception, e:
        return(str(e))

@app.route('/header.py')
def headerpython():
    try:
        gc.collect()
        return render_template("header.py")
    except Exception, e:
        return(str(e))


@app.errorhandler(404)
def page_not_found(e):
    try:
        gc.collect()
        rule = request.path
        if "feed" in rule or "favicon" in rule or "wp-content" in rule or "wp-login" in rule or "wp-login" in rule or "wp-admin" in rule or "xmlrpc" in rule or "tag" in rule or "wp-include" in rule or "style" in rule or "apple-touch" in rule or "genericons" in rule or "topics" in rule or "category" in rule or "index" in rule or "include" in rule or "trackback" in rule or "download" in rule or "viewtopic" in rule or "browserconfig" in rule:
            pass
        else:
            pass
        #flash(str(rule))
        return render_template('404.html'), 404
    except Exception as e:
        return(str(e))

@app.errorhandler(500)
def page_not_found(e):
    return ("Ouch, looks like we're knocked out"), 500


# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/user/change-password/', methods=['GET', 'POST'])
@login_required
def change_password():
    try:
        c,conn = connection()
        
        error = None
        if request.method == 'POST':

            data = c.execute("SELECT * FROM users WHERE username = (%s)",
                    thwart(user.username()))
            data = c.fetchone()[2]


            if sha256_crypt.verify(request.form['password'], data):
                flash('Authentication Successful.')
                if len(request.form['npassword']) > 0:
                    #flash("You wanted to change password")
                    
                    if request.form['npassword'] == request.form['rnpassword'] and len(request.form['npassword']) > 0:
                        try:
                            #flash("new passwords matched")
                            password = sha256_crypt.encrypt((str(request.form['npassword'])))
                            
                            c,conn = connection()
                            
                            data = c.execute("UPDATE users SET password = %s where username = %s",
                            (password,thwart(user.username())))

                            conn.commit()
                            c.close()
                            conn.close()
                            flash("Password changed")
                        except Exception, e:
                            return(str(e))
                    else:
                        flash("Passwords do not match!")

                return render_template('change-password.html', name=user.username(), error=error)

            

            else:
                flash('Invalid credentials. Try again')
                error = 'Invalid credentials. Try again'
        gc.collect()          
        return render_template('change-password.html', name=user.username())#, error=error)
    except Exception, e:
        return(str(e))


@app.route('/login/', methods=['GET','POST'])
def login():
    try:
        c,conn = connection()
        
        error = None
        if request.method == 'POST':

            data = c.execute("SELECT * FROM users WHERE username = (%s)",
                    thwart(request.form['username']))
            data = c.fetchone()[2]

            if sha256_crypt.verify(request.form['password'], data):
                session['logged_in'] = True
                session['username'] = request.form['username']
                #flash('You are now logged in.'+str(session['username']))
                return redirect(url_for('dashboard'))

            else:
                error = 'Invalid credentials. Try again'
        gc.collect()
        return render_template('login.html', error=error)
    except Exception, e:
        error = 'Invalid credentials. Try again'
        return render_template('login.html', error=error)

    

@app.route('/logout/')
def logout():
	session.pop('logged_in', None)
	session.clear()
	flash('You have been logged out.')
	gc.collect()
	return redirect(url_for('main'))


@app.route('/register/', methods=['GET', 'POST'])
def register():

    try:
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate():
            #flash("register attempted")

            username = form.username.data
            email = form.email.data

            password = sha256_crypt.encrypt((str(form.password.data)))
            c,conn = connection()

            x = c.execute("SELECT * FROM users WHERE username = (%s)",
                (thwart(username)))

            if int(x) > 0:
                flash("That username is already taken, please choose another")
                return render_template('register.html', form=form)

            else:
                c.execute("INSERT INTO users (username, password, email, tracking) VALUES (%s, %s, %s, %s)",
                    (thwart(username), thwart(password), thwart(email), thwart("/introduction-to-python-programming/")))
                conn.commit()
                flash('Thanks for registering')
                c.close()
                conn.close()
                gc.collect()
                session['logged_in'] = True
		session['username'] = username
                return redirect(url_for('intro_to_py'))
        gc.collect()
        #flash("hi there.")
        return render_template('register.html', form=form)
    except Exception as e:
        return(str(e))


def topic_completion_percent():
    try:
        client_name, settings, tracking, rank = userinformation()

        try:
            tracking = tracking.split(",")
        except:
            pass

        if tracking == None:
            tracking = []
            #flash("tracking is none")

        completed_percentages = {}
        
        for each_topic in TOPIC_DICT:
            total = 0
            total_complete = 0
            
            for each in TOPIC_DICT[each_topic]:
                total += 1
                for done in tracking:
                    if done == each[1]:
                        total_complete += 1

            percent_complete = int(((total_complete*100)/total))
            completed_percentages[each_topic] = percent_complete


        return completed_percentages
    except:
        for each_topic in TOPIC_DICT:
            total = 0
            total_complete = 0
       
            completed_percentages[each_topic] = 0.0

        return completed_percentages

    pass
    #return basics,pygame,pyopengl,kivy,flask,django,mysql,sqlite,datamanip,dataviz,nltk,svm,clustering,imagerec,forexalgo,robotics,supercomp,tkinter
    
@app.route('/guided-tutorials/', methods=['GET', 'POST'])
@app.route('/topics/', methods=['GET', 'POST'])
@app.route('/begin/', methods=['GET', 'POST'])
@app.route('/python-programming-tutorials/', methods=['GET', 'POST'])
@app.route('/dashboard/', methods=['GET', 'POST'])
#@login_required
def dashboard():
    try:
        try:
            client_name, settings, tracking, rank = userinformation()
            if len(tracking) < 10:
                tracking = "/introduction-to-python-programming/"
            gc.collect()

            if client_name == "Guest":
                flash("Welcome Guest, feel free to browse content. Progress tracking is only available for Logged-in users.")
                tracking = ['None']

            update_user_tracking()

            completed_percentages = topic_completion_percent()

            return render_template("dashboard.html",topics = TOPIC_DICT, tracking = tracking, completed_percentages=completed_percentages)
        except Exception, e:
            return((str(e), "please report errors to hskinsley@gmail.com"))
    except Exception, e:
        return((str(e), "please report errors to hskinsley@gmail.com"))


if __name__ == "__main__":
    app.run()

    
