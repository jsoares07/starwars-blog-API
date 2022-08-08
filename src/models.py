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
            "uid": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class People(db.Model):
    __tablename__ = 'people'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    birth_year = db.Column(db.String(15), nullable=True)
    gender = db.Column(db.String(120), nullable=False)
    hair_color = db.Column(db.String(120), nullable=False)
    eye_color = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<People %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "birth_year": self.birth_year,
            "gender": self.gender,
            "hair_color": self.hair_color,
            "eye_color": self.eye_color,
        }

    def create_people(name, birth_year, gender, hair_color, eye_color):
        people = People(name=name, birth_year=birth_year, gender=gender, hair_color=hair_color, eye_color=eye_color)
        db.session.add(people)
        db.session.commit()

    def get_people(uid):
        people = People.query.filter_by(uid=uid).first()
        return People.serialize(people)

    def get_all_people():
        all_people = People.query.all()
        all_people = list(map(lambda people: people.serialize(), all_people))
        return all_people

    def delete_people(uid):
        people = People.query.get(uid)
        db.session.delete(people)
        db.session.commit()

class Planets(db.Model):
    __tablename__ = 'planets'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(15), nullable=False)
    diameter = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Planets %r>' % self.name

    def serialize(self):
        return {
            "uid": self.id,
            "name": self.name,
            "climate": self.climate,
            "diameter": self.diameter,
            "population": self.population

        }


    def create_planets(name, climate, diameter, population):
        planets = Planets(name=name, climate=climate, diameter=diameter, population=population)
        db.session.add(planets)
        db.session.commit()

    def get_planets(uid):
        planets = Planets.query.filter_by(uid=uid).first()
        return Planets.serialize(planets)

    def get_all_planets():
        all_planets = Planets.query.all()
        all_planets = list(map(lambda planets: planets.serialize(), all_planets))
        return all_planets

    def delete_planets(uid):
        planets = Planets.query.get(uid)
        db.session.delete(planets)
        db.session.commit()


class Favourites(db.Model):
    __tablename__ = 'favourites'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(120), nullable=False)
    favouritetype = db.Column(db.String(120), nullable=False)
    favourite_id = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<Favourites %r>' % self.name

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "favouritetype": self.favouritetype,
            "favourite_id": self.favourite_id,
        }


    @classmethod
    def get_all(cls):
        users = cls.query.all()
        return users