class Product:
    def __init__(self, name, description, stock_quantity, buying_cost, selling_price, vendor, id=None):
        self.name = name
        self.description = description
        self.stock_quantity = stock_quantity
        self.buying_cost = buying_cost
        self.selling_price = selling_price
        self.vendor = vendor
        self.id = id

    def calculate_profit(self):
        profit = (((self.selling_price - self.buying_cost) / self.selling_price) * 100)
        return profit

    def get_three_lowest_stock(self, list_of_products):
        lowest_stock = []
        for i in range(3):
            smallest_temp = list_of_products[0]
            for product in list_of_products:
                if product.stock_quantity < smallest_temp.stock_quantity and product not in lowest_stock:
                    smallest_temp = product
            lowest_stock.append(smallest_temp)
        return lowest_stock
