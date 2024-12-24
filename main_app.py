from datetime import datetime

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from models import db
from routes import main

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

csrf = CSRFProtect()
csrf.init_app(app)

db.init_app(app)
with app.app_context():
    db.create_all()


@app.route("/date_time")
def date_time():
    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


app.register_blueprint(main)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8181, debug=True)
