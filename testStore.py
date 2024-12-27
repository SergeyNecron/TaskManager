import unittest
from store import Store

class TestStore(unittest.TestCase):
    def test_init(self):
        store = Store("Магазин", "ул. Долгая, 12")
        self.assertEqual(store.name, "Магазин")
        self.assertEqual(store.address, "ул. Долгая, 12")
        self.assertEqual(store.items, {})

    def test_add_item(self):
        store = Store("Магазин", "ул. Долгая, 12")
        store.add_item("яблоки", 0.5)
        self.assertIn("яблоки", store.items)
        self.assertEqual(store.items["яблоки"], 0.5)

    def test_remove_item(self):
        store = Store("Магазин", "ул. Долгая, 12")
        store.add_item("яблоки", 0.5)
        store.remove_item("яблоки")
        self.assertNotIn("яблоки", store.items)

    def test_get_item_price(self):
        store = Store("Магазин", "ул. Долгая, 12")
        store.add_item("яблоки", 0.5)
        self.assertEqual(store.get_item_price("яблоки"), 0.5)
        self.assertIsNone(store.get_item_price("бананы"))

    def test_update_item_price(self):
        store = Store("Магазин", "ул. Долгая, 12")
        store.add_item("яблоки", 0.5)
        store.update_item_price("яблоки", 1.0)
        self.assertEqual(store.get_item_price("яблоки"), 1.0)

    def test_update_item_price_non_existent(self):
        store = Store("Магазин", "ул. Долгая, 12")
        store.add_item("яблоки", 0.5)
        store.update_item_price("бананы", 1.0)
        self.assertEqual(store.get_item_price("бананы"), None)

    def test_remove_item_non_existent(self):
        store = Store("Магазин", "ул. Долгая, 12")
        store.remove_item("яблоки")
        self.assertEqual(store.get_item_price("яблоки"), None)

if __name__ == "__main__":
    unittest.main()