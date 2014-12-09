from flask import Flask, jsonify, make_response, abort, request
from classes import *

app = Flask(__name__)
app.json_encoder = MyJSONEncoder

items = [Item(item_id=1, start_time=0, end_time=10, start_price=Price(value=5, currency='USD'),
              address=Address(country='Russia', town='Tomsk'), seller=User('user1'),
              bids=[Bid(bid_time=12, price=Price(value=6, currency='USD'), owner=User('bidder1')),
                    Bid(bid_time=15, price=Price(value=8, currency='USD'), owner=User('bidder2'))]),
         Item(item_id=2, start_time=5, end_time=13, start_price=Price(value=12, currency='EUR'),
              address=Address(country='Russia', town='Barnaul'), seller=User('user2'),
              bids=[Bid(bid_time=12, price=Price(value=15, currency='EUR'), owner=User('bidder1'))])]


@app.route('/items', methods=['GET'])
def get_items():
    return jsonify({'items': items})


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = [x for x in items if x.item_id == item_id]
    if len(item) == 0:
        abort(404)
    return jsonify({'item': item[0]})


@app.route('/items', methods=['POST'])
def create_task():
    if not request.json or \
            not 'start_time' in request.json or \
            not 'end_time' in request.json or \
            not 'start_price' in request.json or \
            not 'address' in request.json or \
            not 'seller' in request.json:
        abort(400)

    item = Item(item_id=1 if len(items) == 0 else items[-1].item_id + 1,
                start_time=request.json.get('start_time'),
                end_time=request.json.get('end_time'),
                start_price=Price(value=request.json.get('start_price')['value'],
                                  currency=request.json.get('start_price')['currency']),
                address=Address(country=request.json.get('address')['country'],
                                town=request.json.get('address')['town']),
                seller=User(login=request.json.get('seller')['login']),
                bids=[])
    items.append(item)
    return jsonify({'item': item}), 201


@app.route('/items/<int:item_id>', methods=['PUT'])
def update_task(item_id):
    item = [x for x in items if x.item_id == item_id]
    if not request.json or len(item) == 0 or \
            'start_time' in request.json and type(request.json['start_time']) != int or \
            'end_time' in request.json and type(request.json['end_time']) != int:
        abort(404)

    item = item[0]
    item.start_time = request.json.get('start_time', item.start_time)
    item.end_time = request.json.get('end_time', item.end_time)

    if 'start_price' in request.json:
        item.start_price.value = request.json['start_price']['value']
        item.start_price.currency = request.json['start_price']['currency']

    if 'address' in request.json:
        item.address.country = request.json.get('address')['country']
        item.address.town = request.json.get('address')['town']

    if 'seller' in request.json:
        item.seller.login = request.json['seller']['login']

    return jsonify({'item': item})


@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_task(item_id):
    item = [x for x in items if x.item_id == item_id]
    if len(item) == 0:
        abort(404)
    items.remove(item[0])
    return jsonify({'result': True})


if __name__ == '__main__':
    app.run(debug=True)
