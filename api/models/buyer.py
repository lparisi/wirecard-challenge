from db import db
class BuyerModel(db.Model):

    __tablename__ = "buyers"

    id = db.Column(db.Integer , primary_key = True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    cpf = db.Column(db.String(100))
    card = db.relationship('CardModel', backref=db.backref('buyer') , lazy='dynamic')
    payment = db.relationship('PaymentModel', backref=db.backref('buyer') ,lazy='dynamic')
    boleto = db.relationship('BoletoModel', backref=db.backref('buyer') ,lazy='dynamic')
    
    def __init__(self, name, email , cpf):
        self.name = name
        self.email = email
        self.cpf = cpf


    def json(self):
        return {
                'name':self.name , 'email':self.email ,'cpf':self.cpf ,
                'card':[c.json() for c in self.card.all()],
                'boleto': [b.json() for b in self.boleto.all()],
                'payment':[p.json() for p in self.payment.all()]
            }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
        

        
