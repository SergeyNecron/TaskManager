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
    # Создание четырех магазинов
    store1 = Store("Магазин 1", "ул. Долгая, 12")
    store2 = Store("Магазин 2", "ул. Широкая, 34")
    store3 = Store("Магазин 3", "ул. Тихая, 56")
    store4 = Store("Магазин 4", "ул. Уголная, 78")

    # Добавление товаров в магазины
    store1.add_item("яблоки", 0.5)
    store1.add_item("бананы", 0.75)
    store2.add_item("апельсины", 1.0)
    store3.add_item("груши", 1.25)
    store4.add_item("арбузы", 1.50)

    # Проверка цен товаров в магазинах
    print(f"Цена яблоки в Магазине 1: {store1.get_item_price('яблоки')}")
    print(f"Цена бананов в Магазине 2: {store2.get_item_price('бананы')}")
    print(f"Цена груш в Магазине 3: {store3.get_item_price('груши')}")
    print(f"Цена арбуза в Магазине 4: {store4.get_item_price('арбузы')}")

    # Обновление цен товаров в магазинах
    store1.update_item_price("яблоки", 0.75)
    store2.update_item_price("апельсины", 1.25)

    # Проверка обновленных цен в магазинах
    print(f"Цена яблоки в Магазине 1 после обновления: {store1.get_item_price('яблоки')}")
    print(f"Цена апельсинов в Магазине 2 после обновления: {store2.get_item_price('апельсины')}")

    # Удаление товаров из магазинов
    store3.remove_item("груши")
    store4.remove_item("арбузы")

    # Проверка удаленных товаров в магазинах
    print(f"Цена груш в Магазине 3 после удаления: {store3.get_item_price('груши')}")
    print(f"Цена арбуза в Магазине 4 после удаления: {store4.get_item_price('арбузы')}")