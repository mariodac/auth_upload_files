import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory, flash
from werkzeug.utils import secure_filename

uploader = Flask(__name__)
uploader.config['MAX_CONTENT_LENGTH'] = 5 * 2048 * 2048
uploader.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.mp4']
uploader.config['UPLOAD_PATH'] = 'static/uploads/'

def validate_image(stream):
    header = stream.read(512)
    stream.seek(0)
    format = imghdr.what(None, header)
    if not format:
        print("not format")
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@uploader.errorhandler(413)
def too_large(e):
    return "File is too large", 413

@uploader.route('/uploads')
def index():
    files = os.listdir(uploader.config['UPLOAD_PATH'])
    return render_template('upload.html', files=files)

@uploader.route('/uploads', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    # filename = filename.replace('', '-')
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in uploader.config['UPLOAD_EXTENSIONS']:
            return "Invalid image", 400
        uploaded_file.save(os.path.join(uploader.config['UPLOAD_PATH'], filename))
    print('arquivo enviado')
    flash('You were successfully logged in')
    return '', 204

@uploader.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(uploader.config['UPLOAD_PATH'], filename)