from flask.json import JSONEncoder
from item.models import Item, Address, Bid, Price
from order.models import Order
from user.models import User

items = [Item(item_id=1, start_time=0, end_time=10, start_price=Price(value=5, currency='USD'),
              address=Address(country='Russia', town='Tomsk'), seller=User('user1'),
              bids=[Bid(bid_time=12, price=Price(value=6, currency='USD'), owner=User('bidder1')),
                    Bid(bid_time=15, price=Price(value=8, currency='USD'), owner=User('bidder2'))]),
         Item(item_id=2, start_time=5, end_time=13, start_price=Price(value=12, currency='EUR'),
              address=Address(country='Russia', town='Barnaul'), seller=User('user2'),
              bids=[Bid(bid_time=12, price=Price(value=15, currency='EUR'), owner=User('bidder1'))])]


class Service(object):
    @staticmethod
    def convert_currency(price, new_currency):
        return Price(price.value * 1.5, new_currency)

    @staticmethod
    def search_items(price_from, price_to):
        return [x for x in items if price_from <= x.start_price.value <= price_to]


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