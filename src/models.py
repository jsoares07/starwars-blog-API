from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }


class Characters(db.Model):
    __tablename__ = 'characters'
    id = db.Column(db.Integer, primary_key=True)
    charName = db.Column(db.String(120), nullable=False)
    charBirthYear = db.Column(db.String(15), nullable=True)
    charGender = db.Column(db.String(15), nullable=True)
    charHairColor = db.Column(db.String(15), nullable=True)
    charEyeColor = db.Column(db.String(15), nullable=True)
    charRel = db.relationship("Favorites")

    def __repr__(self):
        return '<characters %r>' % self.charName


class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    planetName = db.Column(db.String(120), nullable=False)
    planetClimate = db.Column(db.String(15), nullable=False)
    planetDiameter = db.Column(db.Integer, nullable=False)
    planetPopulation = db.Column(db.Integer, nullable=False)
    planetRel = db.relationship("Favorites")

    def __repr__(self):
        return '<planets %r>' % self.planetName


class Vehicles(db.Model):
    __tablename__ = 'vehicles'
    id = db.Column(db.Integer, primary_key=True)
    cargoCapacity = db.Column(db.Integer, nullable=False)
    consumables = db.Column(db.Integer, nullable=False)
    costInCredits = db.Column(db.Integer, nullable=False)
    crew = db.Column(db.Integer, nullable=False)
    manufacturer = db.Column(db.String(30), nullable=False)
    maxSpeed = db.Column(db.Integer, nullable=False)
    model = db.Column(db.String(30), nullable=False)
    passengers = db.Column(db.Integer, nullable=False)
    vehicleRel = db.relationship("Favorites")

    def __repr__(self):
        return '<vehicles %r>' % self.model


class Favorites(db.Model):
    __tablename__ = 'favorites'
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    charId = db.Column(db.Integer, db.ForeignKey("characters.id"), nullable=True)
    vehicleId = db.Column(db.Integer, db.ForeignKey("vehicles.id"), nullable=True)
    planetId = db.Column(db.Integer, db.ForeignKey("planets.id"), nullable=True)

    def __repr__(self):
        return '<favorites %r>' % self.id