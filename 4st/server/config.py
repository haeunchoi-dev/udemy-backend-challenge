import pathlib

import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from openapi_server import encoder

basedir = pathlib.Path(__file__).parent.resolve()
connex_app = connexion.App(__name__, specification_dir='./openapi_server/openapi/')
app = connex_app.app
app.json_encoder = encoder.JSONEncoder

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'book.db'}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
ma = Marshmallow(app)
