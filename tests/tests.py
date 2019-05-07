import unittest
from werkzeug.exceptions import NotFound
from app import create_app, db
from api.models import boleto, buyer, card, client, payment
from .test_client import TestClient


class TestAPI(unittest.TestCase):


    def setUp(self):
        self.app = create_app('testing')
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.drop_all()
        db.create_all()
        db.session.add(u)
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_listpayments(self):
        # get list of customers
        rv, json = self.client.get('/payments/')        #list all payments from endpoint using get
        self.assertTrue(rv.status_code == 200)          #Expected status is 200, OK.
        self.assertTrue(json['payments'] == [])         #Since we dropped the database, should be empty

    def test_getpayment(self):
        # get list of products
        rv, json = self.client.get('/payments/id')
        self.assertTrue(rv.status_code == 200)
        self.assertTrue(json['payments'] == [])


    def test_creatpayment(self):
        # define a customer
        data = {'client': {'id': 1}, 
                'buyer': {
                    'name': 'Julian Casablancas', 
                    'email': 'dustydrums@strokes.com', 
                    'cpf': 33723404855
                    }, 
                'payment': {
                    'amount': 254.37, 
                    'type': 'boleto', 
                    'card': {
                        'cardNumber': '', 
                        'holderName': '', 
                        'month': '', 
                        'year': '', 
                        'cvv': ''
                        }
                    }
                }

        rv, json = self.client.post('/payments/', data) #create a boleto payment using a dict
        self.assertTrue(rv.status_code == 201)          #Expected status is 201, Created. (The request has been fulfilled and has resulted in one or more new resources being created.)
        content_type = rv.headers['Content-Type']
        rv, json = self.client.get(content_type)
        self.assertTrue(rv.status_code == 200)
        self.assertTrue(json['type'] == 'boleto')        #Expected status is 200, OK (The request has succeeded.)
        rv, json = self.client.get('/payments')
        self.assertTrue(rv.status_code == 200)
        self.assertTrue(json['payment'] == [content_type])