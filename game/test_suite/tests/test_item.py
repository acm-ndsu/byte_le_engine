import unittest

from game.common.avatar import Avatar
from game.common.items.item import Item
from game.common.enums import ObjectType


class TestItem(unittest.TestCase):
    """
    `Test Item Notes:`

        This class tests the different methods in the Item class.
    """

    def setUp(self) -> None:
        self.avatar: Avatar = Avatar(None, 1)
        self.item: Item = Item()

    # test set durability
    def test_set_durability(self):
        self.item.durability = 10
        self.assertEqual(self.item.durability, 10)

    def test_set_durability_none(self):
        self.item.durability = None
        self.assertEqual(self.item.durability, None)

    def test_set_durability_fail(self):
        value: str = 'fail'
        with self.assertRaises(ValueError) as e:
            self.item.durability = value
        self.assertEqual(str(e.exception), f'Item.durability must be an int. It is a(n) {value.__class__.__name__} with the value of {value}.')

    def test_set_durability_stack_size_fail(self):
        value: list = Item(10,None,10,10)
        value2: int = 10
        with self.assertRaises(ValueError) as e:
            self.item = value
            self.item.durability = value2
        self.assertEqual(str(e.exception), f'Item.durability must be set to None if stack_size is not equal to 1.'
                                           f' {value.__class__.__name__}.'
                                           f'durability has the value of {value2}.')

    # test set value
    def test_set_value(self):
        self.item.value = 10
        self.assertEqual(self.item.value, 10)

    def test_set_value_fail(self):
        value: str = 'fail'
        with self.assertRaises(ValueError) as e:
            self.item.value = value
        self.assertEqual(str(e.exception), f'Item.value must be an int.'
                                           f' It is a(n) {value.__class__.__name__} with the value of {value}.')

    # test set quantity
    def test_set_quantity(self):
        self.item = Item(10, None, 10, 10)
        self.item.quantity = 5
        self.assertEqual(self.item.quantity, 5)

    def test_set_quantity_fail(self):
        value: str = 'fail'
        with self.assertRaises(ValueError) as e:
            self.item.quantity = value
        self.assertEqual(str(e.exception), f'Item.quantity must be an int.'
                                           f' It is a(n) {value.__class__.__name__} with the value of {value}.')

    def test_set_quantity_fail_greater_than_0(self):
        value: Item = -1
        with self.assertRaises(ValueError) as e:
            self.item.quantity = value
        self.assertEqual(str(e.exception), f'Item.quantity must be greater than or '
                                           f'equal to 0. {self.item.__class__.__name__}.quantity '
                                           f'has the value of {value}.')

    def test_set_quantity_fail_stack_size(self):
        value: Item = 10
        value2: Item = 1
        with self.assertRaises(ValueError) as e:
            self.item.quantity = value
            self.item.stack_size = value2
        self.assertEqual(str(e.exception), f'Item.quantity cannot be greater than '
                             f'{self.item.__class__.__name__}.stack_size. {self.item.__class__.__name__}.quantity has the value of {value}.')

    def test_stack_size(self):
        self.item = Item(10, None, 10, 10)
        self.assertEqual(self.item.quantity, 10)

    def test_stack_size_fail(self):
        value: str = 'fail'
        with self.assertRaises(ValueError) as e:
            self.item.stack_size = value
        self.assertEqual(str(e.exception), f'Item.stack_size must be an int.'
                                           f' It is a(n) {value.__class__.__name__} with the value of {value}.')

    def test_stack_size_fail_quantity(self):
        # value, durability, quantity, stack size
        value: Item = 5
        with self.assertRaises(ValueError) as e:
            item: Item = Item(10, None, 10, 10)
            item.stack_size = value
        self.assertEqual(str(e.exception), f'Item.stack_size must be greater than or equal to the quantity.'
                                           f' {self.item.__class__.__name__}.stack_size has the value of {value}.')

    def test_pick_up(self):
        # value, durability, quantity, stack size
        item: Item = Item(10, None, 2, 10)
        self.item = Item(10, None, 1, 10)
        self.item.pick_up(item)
        self.assertEqual(self.item.quantity, 3)

    def test_pick_up_wrong_object_type(self):
        item: Item = Item(10, 10, 1, 1)
        item.object_type = ObjectType.PLAYER
        self.item = Item(10, 10, 1, 1)
        self.item = self.item.pick_up(item)
        self.assertEqual(self.item.object_type, item.object_type)

    def test_pick_up_surplus(self):
        item: Item = Item(10, None, 10, 10)
        self.item = Item(10, None, 9, 10)
        surplus: Item = self.item.pick_up(item)
        self.assertEqual(surplus.quantity, 9)

    def test_item_json(self):
        data: dict = self.item.to_json()
        item: Item = Item().from_json(data)
        self.assertEqual(self.item.object_type, item.object_type)
        self.assertEqual(self.item.value, item.value)
        self.assertEqual(self.item.stack_size, item.stack_size)
        self.assertEqual(self.item.durability, item.durability)
        self.assertEqual(self.item.quantity, item.quantity)
