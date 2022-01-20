
from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    email = db.Column(db.String(150), unique=True) # Vill inte ha två användare med samma epost
    password = db.Column(db.String(100))
    admin = db.Column(db.BOOLEAN, default=False)

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id # Man kan också returnera email här