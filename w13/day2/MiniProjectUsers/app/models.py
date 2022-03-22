from app import db


class User(db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    userName = db.Column(db.String(50))
    userStreet = db.Column(db.String(100))
    userCity = db.Column(db.String(100))
    zipCode = db.Column(db.String(50))

    def __str__(self):
        return f""" 
        ID number: {self.user_id}, User Name: {self.userName}\n 
        User Street: {self.userStreet}, User City: {self.userCity} and Zipcode: {self.zipCode}\n
        """


db.create_all()  # I had a problem with the bd in the __init__ couldn't recognize the User class from models,
# for some reason, found this solution on stackoverflow.
