from app import db
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    balance = db.Column(db.Integer, nullable=False)
    card_number = db.Column(db.String(16), unique=True, nullable=False)
    card_date = db.Column(db.Date, nullable=False)
    def __init__(self, username, email, password, balance, card_number, card_date):
        self.username = username
        self.email = email
        self.password = password
        self.balance = balance
        self.card_number = card_number
        self.card_date = card_date
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    card_number = db.Column(db.String(16), unique=True, nullable=False)
    card_date = db.Column(db.Date, nullable=False)
    transaction_date = db.Column(db.Date, nullable=False)

    def __init__(self, card_number, card_date, transaction_date):
        self.card_number = card_number
        self.card_date = card_date
        self.transaction_date = transaction_date
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
