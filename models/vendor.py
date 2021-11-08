class Vendor:
    def __init__(self, name, active, id=None):
        self.name = name
        self.active = active
        self.id = id
        self.products = []
