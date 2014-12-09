from flask.json import JSONEncoder


class Item(object):
    def __init__(self, item_id, start_time, end_time, start_price, address, seller, bids):
        self.item_id = item_id
        self.start_time = start_time
        self.end_time = end_time
        self.start_price = start_price
        self.address = address
        self.seller = seller
        self.bids = bids


class Order(object):
    def __init__(self, place_time, item):
        self.place_time = place_time
        self.item = item


class Address(object):
    def __init__(self, country, town):
        self.country = country
        self.town = town


class User(object):
    def __init__(self, login):
        self.login = login


class Bid(object):
    def __init__(self, bid_time, price, owner):
        self.bid_time = bid_time
        self.price = price
        self.owner = owner


class Price(object):
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency


class Service(object):
    @staticmethod
    def convert_currency(price, new_currency):
        return Price(price.value, new_currency)

    @staticmethod
    def search_items(price_from, price_to):
        return []


class MyJSONEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, User):
            return {
                'login': obj.login,
            }
        elif isinstance(obj, Price):
            return {
                'value': obj.value,
                'currency': obj.currency,
            }
        elif isinstance(obj, Bid):
            return {
                'bid_time': obj.bid_time,
                'price': obj.price,
                'owner': obj.owner,
            }
        elif isinstance(obj, Address):
            return {
                'country': obj.country,
                'town': obj.town,
            }
        elif isinstance(obj, Order):
            return {
                'place_time': obj.place_time,
                'item': obj.item,
            }
        elif isinstance(obj, Item):
            return {
                'item_id': obj.item_id,
                'start_time': obj.start_time,
                'end_time': obj.end_time,
                'start_price': obj.start_price,
                'address': obj.address,
                'seller': obj.seller,
                'bids': obj.bids,
            }
        return super(MyJSONEncoder, self).default(obj)