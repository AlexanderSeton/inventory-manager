class Vendor:
    def __init__(self, name, active=True, id=None):
        self.name = name
        self.active = active
        self.id = id
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def check_active(self):
        if self.active:
            return True
        return False
    
    def set_active(self):
        self.active = True
    
    def set_inactive(self):
        self.active = False
