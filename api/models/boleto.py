from db import db
class BoletoModel(db.Model):

    __tablename__ = "boletos"

    id = db.Column(db.Integer , primary_key = True)
    number = db.Column(db.String(100))
    buyer_id = db.Column(db.Integer,db.ForeignKey('buyers.id'))
    payment = db.relationship('PaymentModel', backref=db.backref('boleto'))

    def __init__(self, number , buyer_id):
        self.number = number
        self.buyer_id = buyer_id

    
    def json(self):
        return {'number':self.number }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
   
