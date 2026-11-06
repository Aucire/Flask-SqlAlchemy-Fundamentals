from flask import Flask
from flask_migrate import Migrate

from model import db, Application, Doctor
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test_table.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


if __name__ == '__main__':
    app.run(debug=True)