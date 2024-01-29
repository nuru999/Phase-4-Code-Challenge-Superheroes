from flask import Blueprint, jsonify, request
from models import db, Hero, Power, HeroPower

api = Blueprint('api', __name__)

@api.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])

@api.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.serialize())
    else:
        return jsonify({'message': 'Hero not found'}), 404

@api.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.serialize() for power in powers])

@api.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.serialize())
    else:
        return jsonify({'message': 'Power not found'}), 404

@api.route('/heroes/<int:hero_id>/powers', methods=['GET'])
def get_hero_powers(hero_id):
    hero = Hero.query.get(hero_id)
    if hero:
        powers = [hero_power.power.serialize() for hero_power in hero.hero_powers]
        return jsonify(powers)
    else:
        return jsonify({'message': 'Hero not found'}), 404

# Add more routes as specified in the project requirements

