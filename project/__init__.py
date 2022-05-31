from fileinput import filename
from flask import Flask, render_template, request, redirect, url_for, abort, send_from_directory, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from werkzeug.utils import secure_filename
import logging 
import imghdr
import os


# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()

log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logger = logging.getLogger(__name__)
# To override the default severity of logging
logger.setLevel('DEBUG')

# Use FileHandler() to log to a file
file_handler = logging.FileHandler("info.log")
formatter = logging.Formatter(log_format)
file_handler.setFormatter(formatter)

# Don't forget to add the file handler
logger.addHandler(file_handler)
def create_app():
    logging.basicConfig(filename='debug.log',level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
    app.config['MAX_CONTENT_LENGTH'] = 5 * 2048 * 2048
    app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif', '.mp4', '.avi', '.mpeg']
    app.config['UPLOAD_PATH'] = 'project/static/uploads/'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)
    
    from .models import User
    
    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        logger.info('User %s loaded', user_id)
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # blueprint for non-auth parts of app
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    
    def validate_image(stream):
        header = stream.read(512)
        stream.seek(0)
        format = imghdr.what(None, header)
        if not format:
            logger.info('File with no format')
            print("not format")
            return None
        return '.' + (format if format != 'jpeg' else 'jpg')

    @app.errorhandler(413)
    def too_large(e):
        logger.info('File is too large')
        return "File is too large", 413

    @app.route('/uploads', methods=['POST'])
    def upload_files():
        uploaded_file = request.files['file']
        filename = secure_filename(uploaded_file.filename)
        # filename = filename.replace('', '-')
        if filename != '':
            file_ext = os.path.splitext(filename)[1]
            if file_ext not in app.config['UPLOAD_EXTENSIONS']:
                return "Invalid image", 400
            save_file = os.path.join(app.config['UPLOAD_PATH'], filename)
            uploaded_file.save(save_file)
            logger.info('File save in %s',save_file)
        # print('arquivo enviado')
        return '', 204

    @app.route('/uploads/<filename>')
    def upload(filename):
        return send_from_directory(app.config['UPLOAD_PATH'], filename)

    return app