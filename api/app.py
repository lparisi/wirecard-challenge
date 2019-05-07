from flask import Flask
from flask_restful import Api
from resources.payment import CreatePayment , ListPayments , GetPayment
from db import db

app = Flask(__name__)
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.secret_key = 'jose'
api = Api(app)
db.init_app(app)

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(CreatePayment, '/payments')
api.add_resource(GetPayment, '/payments/<int:id>')
api.add_resource(ListPayments, '/payments')

if __name__ == '__main__':
    app.run(debug=True)
    