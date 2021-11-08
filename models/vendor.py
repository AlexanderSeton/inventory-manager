class Vendor:
    def __init__(self, name, active=True, id=None):
        self.name = name
        self.active = active
        self.id = id

    def check_active(self):
        if self.active:
            return True
        return False
    
    def set_active(self):
        self.active = True
    
    def set_inactive(self):
        self.active = False
