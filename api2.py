from flask import Flask 
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

orders = []

class Orders(Resource):
    def get(self):
        return orders

    def post(self):
        #Alternative https://marshmallow.readthedocs.io/en/3.0/
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('price')
        args = parser.parse_args()
        orders.append(args)
        return orders
     
class Order(Resource): 
    def get(self, index):
        return orders[int(index)]

    def put(self, index):
        parser = reqparse.RequestParser()
        parser.add_argument('name')
        parser.add_argument('price')
        args = parser.parse_args()
        orders[int(index)].update(args)
        return orders

class User(Resource):
    def get(self):
        return {'username': 'ziana'}

api.add_resource(Orders,'/v1/orders')
api.add_resource(Order,'/v1/orders/<index>')
api.add_resource(User,'/v1/users')

if __name__ == '__main__':
    app.run(debug=True)
