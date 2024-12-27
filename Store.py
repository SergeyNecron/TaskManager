class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        if item_name in self.items:
            print(f"Товар '{item_name}' уже есть в ассортименте.")
        else:
            self.items[item_name] = price
            print(f"Товар '{item_name}' добавлен в ассортимент.")

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар '{item_name}' удален из ассортимента.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")

    def get_item_price(self, item_name):
        return self.items.get(item_name)

    def update_item_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Цена товара '{item_name}' обновлена.")
        else:
            print(f"Товар '{item_name}' не найден в ассортименте.")


if __name__ == "__main__":
    store = Store("Магазин", "ул. Долгая, 12")
    store.add_item("яблоки", 0.5)
    store.add_item("бананы", 0.75)

    print(store.get_item_price("яблоки"))  # Вывод: 0.5
    print(store.get_item_price("бананы"))  # Вывод: 0.75

    store.update_item_price("яблоки", 1.0)
    print(store.get_item_price("яблоки"))  # Вывод: 1.0

    store.remove_item("бананы")
    print(store.get_item_price("бананы"))  # Вывод: None