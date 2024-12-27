class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}  # Словарь для ассортимента

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

if __name__ == "__main__":
    store = Store("Fruit Shop", "123 Main St")
    store.add_item("apples", 0.5)
    store.add_item("bananas", 0.75)

    print(store.items)  # {'apples': 0.5, 'bananas': 0.75}

    print(store.get_price("apples"))  # 0.5
    print(store.get_price("oranges"))  # None

    store.update_price("apples", 0.6)
    print(store.get_price("apples"))  # 0.6

    store.remove_item("bananas")
    print(store.items)  # {'apples': 0.6}