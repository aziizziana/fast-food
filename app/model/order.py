
class Order:
    def __init__(self, identifier, name, price, status):
        self.identifier = identifier
        self.name = name
        self.price = price

    def get_dict(self):
        return dict(identifier=self.identifier, name=self.name, price=self.price, status=self.status)
    
    def generate_random_key(self):
        :return:
        return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits)for_in range(10))