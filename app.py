from flask import Flask, request, jsonify
from models import db, Hero, Power, HeroPower

app = Flask(__name)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    return jsonify([hero.serialize() for hero in heroes])

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    if hero:
        return jsonify(hero.serialize())
    else:
        return jsonify({'message': 'Hero not found'}), 404

@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.serialize() for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    if power:
        return jsonify(power.serialize())
    else:
        return jsonify({'message': 'Power not found'}), 404

# Implement routes for POST and PATCH (create and update)

if __name__ == '__main':
    with app.app_context():
        db.create_all()
    app.run(port=5555, debug=True)
