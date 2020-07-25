import os
import boto3
from flask import Flask, render_template, request, flash, url_for, session
from utils import list_files, upload_file_s3
from functools import wraps
from werkzeug.utils import redirect
from config import *

app = Flask(__name__)
app.config.from_object("config")
app.secret_key = SECRET_KEY
s3_client = boto3.client('s3', aws_access_key_id=S3_ACCESS_KEY, aws_secret_access_key=S3_SECRET_ACCESS_KEY)


def login_required(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return func(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap


@app.route('/')
def entry_point():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
            session.clear()
        else:
            session['logged_in'] = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/home')
@login_required
def home():
    return render_template('home.html')


@app.route("/list")
@login_required
def list_bucket():
    contents = list_files(s3_client, S3_BUCKET_NAME, S3_LOCATION)
    return render_template('file-list.html', contents=contents)


@app.route("/file_upload", methods=['GET'])
@login_required
def file_upload():
    return render_template('upload.html')


@app.route("/upload", methods=['POST'])
@login_required
def upload():
    if request.method == "POST":
        file = request.files['file']
        file.save(file.filename)
        upload_file_s3(s3_client, file.filename, S3_BUCKET_NAME)
        os.remove(file.filename)
        return redirect(url_for('list_bucket'))


@app.route('/logout')
@login_required
def logout():
    if 'logged_in' in session:
        session.clear()
    flash('You have successfully logged yourself out.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)
