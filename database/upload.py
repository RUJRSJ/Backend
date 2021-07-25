import flask
import pandas as pd
import pyreadstat as prs
from flask import Flask, Blueprint, request
from werkzeug.utils import secure_filename

__all__ = ['Upload_Files']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

class Upload_Files():
    def __init__(self, username):
        self.user = username

    def get_user_folder(self):
        #get user folder path
        file_dir = os.path.join(fileApp_api.config['UPLOAD_FOLDER'] , self.user)
        #create user folder if not exist
        if not os.path.exists(file_dir):
                os.makedirs(file_dir)
        return file_dir

    def get_file(self, request):
        # check if the post request has the file part
        if 'file' not in request.files:
            return "No files"
        file = request.files['file']

        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            return "No files"
        
        #there is file
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(self.get_user_folder(), filename)
            file.save(file_path)
        return file_path