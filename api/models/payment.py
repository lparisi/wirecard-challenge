from db import db
class PaymentModel(db.Model):

    __tablename__ = "payments"

    id = db.Column(db.Integer , primary_key = True)
    u_id = db.Column(db.String(100))
    amount = db.Column(db.Float(precision=2))
    type = db.Column(db.String(100))
    buyer_id = db.Column(db.Integer,db.ForeignKey('buyers.id'))
    card_id = db.Column(db.Integer,db.ForeignKey('cards.id') , nullable=True)
    boleto_id = db.Column(db.Integer,db.ForeignKey('boletos.id') , nullable=True)
    
    def __init__(self, u_id, amount , type , buyer_id , card_id , boleto_id):
        self.u_id = u_id
        self.amount = amount
        self.type = type
        self.buyer_id = buyer_id
        self.card_id = card_id
        self.boleto_id = boleto_id

    def json(self):
        return {'u_id':self.u_id, 'amount':self.amount , 'type':self.type  }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


        
