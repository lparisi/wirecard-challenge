from flask_restful import Resource , request 
from werkzeug.security import safe_str_cmp
import pycard
import re
from models.buyer import BuyerModel
from models.payment import PaymentModel
from models.card import CardModel
from models.boleto import BoletoModel
import random
import uuid

class Payment(Resource):
    def post(self):
        data = request.get_json()

        #buyer information
        name = data['buyer']['name']
        email = data['buyer']['email']
        cpf = data['buyer']['cpf']
        if not re.search(r'\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b', email, re.I):
            return {'response':'Invalid email address'} , 400
            

        # payment information
        type = data['payment']['type'].lower()
        amount = data['payment']['amount']

        if safe_str_cmp(type , 'credit_card'):

            cardnumber = data['payment']['card']['cardNumber']
            holderName = data['payment']['card']['holderName']
            month = data['payment']['card']['month']
            year = data['payment']['card']['year']
            cvc = data['payment']['card']['cvv']

            picard = pycard.Card(
                number = cardnumber,
                month = month,
                year = year,
                cvc = cvc
            ) 
            if picard.is_valid and not picard.is_expired:
                u_id = str(uuid.uuid1())
                
                # Everything needs to be inserted here.
                buyer_ = BuyerModel.find_by_email(email)
                if buyer_:
                    crd = CardModel(cardnumber , month , year , cvc , buyer_.id)
                    crd.save_to_db()
                    PaymentModel(u_id,amount, type , buyer_.id, crd.id , None).save_to_db()
                    return {'response': 'Payment added successfuly!'}, 201
                else:
                    BuyerModel(name , email, cpf).save_to_db()
                    buyer_ = BuyerModel.find_by_email(email)   
                    crd = CardModel(cardnumber , month , year , cvc , buyer_.id)
                    crd.save_to_db()
                    PaymentModel(u_id, amount, type , buyer_.id, crd.id , None).save_to_db()

                    return {'response': 'Payment added successfuly!'}, 201
                
            else:
                return {'response':'Card information is incorrect'},400

        elif safe_str_cmp(type , 'boleto'):   
            u_id = str(uuid.uuid1())
            boleto_number = random.randint(100000000000000000000000000000000000000000000000,999999999999999999999999999999999999999999999999)
            boleto_str = str(boleto_number)
            buyer_ = BuyerModel.find_by_email(email)
            if buyer_:
                blt = BoletoModel(boleto_str, buyer_.id)
                blt.save_to_db()
                PaymentModel(u_id , amount, type , buyer_.id, None, blt.id ).save_to_db()
                return {'response': 'Payment added successfuly!'}, 201
            else:
                BuyerModel(name , email, cpf).save_to_db()
                buyer_ = BuyerModel.find_by_email(email)   
                blt = BoletoModel(boleto_str, buyer_.id)
                blt.save_to_db()
                PaymentModel(u_id , amount, type , buyer_.id, None, blt.id ).save_to_db()
                return {'response': 'Payment added successfuly!'}, 201



class SinglePayment(Resource):
    def get(self, id):
        return {'PaymentsRecords': [buyer.json() for buyer in BuyerModel.query.filter_by(id=id).all()]}

class PaymentList(Resource):
    def get(self):
        return {'PaymentsRecords': [buyer.json() for buyer in BuyerModel.query.all()]}
      