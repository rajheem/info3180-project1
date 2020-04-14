"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/
This file creates your application.
"""
import os
from app import app, db
from flask_login import login_user, logout_user, current_user, login_required
from app.forms import ProfileForm
from app.models import UserProfile
from werkzeug.security import check_password_hash
from flask import render_template, request, redirect, url_for, flash, session, abort
from werkzeug.utils import secure_filename


###
# Routing for your application.
###

@app.route('/')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


@app.route("/profile", methods=["GET", "POST"])
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        fname=request.form['first_name']
        lname=request.form['last_name']
        gender=request.form['gender']
        email=request.form['email']
        location=request.form['location']
        biography=request.form['biography']
        f = request.files['profile_pic']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        new_prof=UserProfile(fname,lname,gender,email,location,biography,filename)
        db.session.add(new_prof)
        db.session.commit()
        flash('Profile Added','success')
        return redirect(url_for('list_profiles'))
    return render_template('profile.html',form=form)

@app.route("/profiles")
def list_profiles():
    profiles=db.session.query(UserProfile).all()
    return render_template("list_profiles.html",profiles=profiles)

@app.route("/profile/<userid>")
def profile_det(userid):
    profile=db.session.query(UserProfile).get(userid)
    if profile:
        return render_template("profile_det.html",profile=profile)
    else:
        return redirect(url_for("list_profiles"))
    
@app.route("/secure-page")
def secure_page():
    return render_template('secure_page.html')


    

# user_loader callback. This callback is used to reload the user object from
# the user ID stored in the session
#@login_manager.user_loader
#def load_user(id):
#    return UserProfile.query.get(int(id))

###
# The functions below should be applicable to all Flask apps.
###


@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=0'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="8080")
