from flask import Flask
from flask_restful import reqparse, abort, Api, Resource, marshal_with, fields
from animalfacts import Facts, db

app = Flask(__name__)
api = Api(app)

fact_fields = {
    'id': fields.Integer,
    'animal': fields.String,
    'fact': fields.String,
}

def abort_if_fact_doesnt_exist(fact_id):
    if Facts.query.get(fact_id) not in Facts.query.all():
        abort(404, message="Fact {} doesn't exist".format(fact_id))

def delete_fact(fact_id):
    fact = Facts.query.get(fact_id)
    db.session.delete(fact)
    db.session.commit()

def add_todo(factAnimal = str, factStr = str):
    fact = Facts(factAnimal, factStr)
    db.session.add(fact)
    db.session.commit()

def update_todo(fact_id, factAnimal = str, factStr = str):
    fact = Facts.query.get(fact_id)
    fact.animal = factAnimal
    fact.fact = factStr
    db.session.commit()

parser = reqparse.RequestParser(bundle_errors=True)
parser.add_argument('animal', type=str, required=True)
parser.add_argument('fact', type=str, required=True)


# Fact
# shows a single fact and lets you delete a fact
class Fact(Resource):
    @marshal_with(fact_fields)
    def get(self, fact_id):
        abort_if_fact_doesnt_exist(fact_id)
        return Facts.query.get(fact_id)

    def delete(self, fact_id):
        abort_if_fact_doesnt_exist(fact_id)
        delete_todo(fact_id)
        return 'Deleted Successfully', 204

    def put(self, fact_id):
    	abort_if_fact_doesnt_exist(fact_id)
        try:
            args = parser.parse_args()
            update_fact(fact_id, args['animal'], args['fact'])
            return fact_id, 201
        except:
            return 'Error has occured', 500


# FactList
# shows a list of all the facts
class FactList(Resource):
    @marshal_with(fact_fields)
    def get(self):
    	try:
        	return Facts.query.all()
        except:
        	return 'Error has occured', 500

    def post(self):
        try:
            args = parser.parse_args()
            add_fact(args['animal'], args['task'])
            return 'Success!', 201
        except:
            return 'Error has occured', 500

# FactAnimal
# Sort the facts by the animal requested
class FactAnimal(Resource):
    @marshal_with(fact_fields)
    def get(self, factAnimal):
        allAnimalFacts = Facts.query.filter_by(animal=factAnimal).all()
        return allAnimalFacts

##
## Actually setup the Api resource routing here
##
api.add_resource(FactList, '/animalfacts')
api.add_resource(Fact, '/animalfacts/fact/<fact_id>')
api.add_resource(FactAnimal, '/animalfacts/animal/<string:factAnimal>')


if __name__ == '__main__':
    app.run()