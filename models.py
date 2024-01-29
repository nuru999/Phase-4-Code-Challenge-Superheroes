from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'super_name': self.super_name,
        }

class Power(db.Model):
    __tablename__ = 'power'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
        }

class HeroPower(db.Model):
    __tablename__ = 'hero_power'
    id = db.Column(db.Integer, primary_key=True)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('power.id'), nullable=False)
    strength = db.Column(db.Integer, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'hero_id': self.hero_id,
            'power_id': self.power_id,
            'strength': self.strength,
        }
