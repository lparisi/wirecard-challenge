from db import db
class CardModel(db.Model):

    __tablename__ = "cards"

    id = db.Column(db.Integer , primary_key = True)
    number = db.Column(db.String(100))
    month = db.Column(db.Integer)
    year = db.Column(db.Integer)
    cvc = db.Column(db.Integer)
    buyer_id = db.Column(db.Integer,db.ForeignKey('buyers.id'))
    payment = db.relationship('PaymentModel', backref=db.backref('card'))

    def __init__(self, number , month , year , cvc , buyer_id):
        self.number = number
        self.month = month
        self.year = year
        self.cvc = cvc
        self.buyer_id = buyer_id

    
    def json(self):
        return {'number':self.number , 'month':self.month ,'year':self.year , 'cvc':self.cvc  }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    @classmethod
    def find_card_number_by_id(cls , _id):
        return cls.query.filter_by(number = cls.number).filter_by(buyer_id=_id).first()


        
