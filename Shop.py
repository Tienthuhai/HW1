class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items
    def get_items_count(self):
        return len(self.items)
shop = Shop("My shop",["Minh","Tu","DucBo"])
print(shop.get_items_count()) 
