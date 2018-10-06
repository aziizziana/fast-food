from flask import Flask, request
from flask_restful import Api, Resource, abort, reqparse

app = Flask(__name__)
api = Api(app)

orders = {}

'''Test if an order does not exist and siplay a clear error message'''
def abort_if_order_doesnt_exist(order_id):
    if order_id not in orders:
        abort(404, message="Order {} doesn't exist".format(order_id))

parser = reqparse.RequestParser()
parser.add_argument('order')
parser.add_argument('price')

#orders = {'order_id': {'my_order': 'fries', 'price': 3000}}

# Show all orders
class Orders(Resource):
    def get(self):
        return {'orders':orders}
    def post(self):
        args = parser.parse_args()
        if not str(args['order']).strip():
            abort(400, message="Order cannot be empty")
        else:
            print("Args is {}".format(args))
            if not orders:
                order_id = 1
            else:
                order_id = int(max(orders.keys()).lstrip('order')) + 1
            order_id = 'order%i' % order_id
            orders[order_id] = {'my_order': args['order'], 'price':args['price']}
            print(orders)
            return orders, 201

# shows a single order and lets you delete an order
class Order(Resource):
    def get(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        return {order_id: orders[order_id]}
    def delete(self, order_id):
        abort_if_order_doesnt_exist(order_id)
        del orders[order_id]

        return 'Order deleted', 204
    def put(self, order_id):
        args = parser.parse_args()
        order = {'my_order': args['order']}
        orders[order_id] = order
        return order, 201

api.add_resource(Orders,'/v1/orders')
api.add_resource(Order, '/v1/orders/<string:order_id>')

