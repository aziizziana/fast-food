from flask import Flask 
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

orders = []

class Order(Resource):
    def get(self):
        return orders

    def post(self):
        orders.append({'name': 'burger', 'price':'2000'})
        ## get user request
        ## add it to the orders
        return orders
class Orders(Resource):
    def get(self, index):
        return orders[int(index)]

class User(Resource):
    def get(self):
        return {'username': 'ziana'}

api.add_resource(Order,'/v1/orders')
api.add_resource(Orders,'/v1/orders/<index>')
api.add_resource(User,'/v1/users')

if __name__ == '__main__':
    app.run(debug=True)

# GET /v1/orders

# POST http://localhost/v1/orders
# PUT /v1/orders
# Overloading occurs when two or more methods in one class have the
# same method name but different parameters