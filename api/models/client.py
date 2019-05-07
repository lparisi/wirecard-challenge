from db import db
class ClientModel(db.Model):

    __tablename__ = "clientes"

    id = db.Column(db.Integer , primary_key = True)
    
    def __init__(self, number , buyer_id):
        self.id = id
        

    
    def json(self):
        return {'number':self.id }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
   
