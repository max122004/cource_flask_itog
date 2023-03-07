from flask import Flask, render_template
from flask_restx import Api

from cource_3.config import Config
from cource_3.setup_db import db
from cource_3.views.auth import auth_ns
from cource_3.views.directors import director_ns
from cource_3.views.genre import genre_ns
from cource_3.views.movie import movie_ns
from cource_3.views.user import user_ns


# функция создания основного объекта app


def create_app(config_object):
    application = Flask(__name__, template_folder='templates')
    application.config.from_object(config_object)

    # @application.route('/')
    # def index():
    #     return render_template('index.html')

    register_extensions(application)
    return application
#
#
# функция подключения расширений (Flask-SQLAlchemy, Flask-RESTx, ...)
def register_extensions(application):
    db.init_app(application)
    api = Api(application)
    api.add_namespace(movie_ns)
    api.add_namespace(genre_ns)
    api.add_namespace(director_ns)
    api.add_namespace(user_ns)
    api.add_namespace(auth_ns)



if __name__ == '__main__':
    app_config = Config()
    app = create_app(app_config)
    app.run()
