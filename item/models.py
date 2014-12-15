class Item(object):
    def __init__(self, item_id, start_time, end_time, start_price, address, seller, bids):
        self.item_id = item_id
        self.start_time = start_time
        self.end_time = end_time
        self.start_price = start_price
        self.address = address
        self.seller = seller
        self.bids = bids


class Bid(object):
    def __init__(self, bid_time, price, owner):
        self.bid_time = bid_time
        self.price = price
        self.owner = owner


class Price(object):
    def __init__(self, value, currency):
        self.value = value
        self.currency = currency

        
class Address(object):
    def __init__(self, country, town):
        self.country = country
        self.town = town