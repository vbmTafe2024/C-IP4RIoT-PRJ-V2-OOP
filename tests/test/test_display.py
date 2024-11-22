import unittest
from display import Display
from carPark import CarPark


class TestDisplay(unittest.TestCase):
    def setUp(self):
        self.car_park = CarPark("123 Example Street", 50)
        self.display = Display(id=1, message="Welcome to the car park", is_on=True, car_park=self.car_park)

    def test_display_initialized_with_all_attributes(self):
        self.assertIsInstance(self.display, Display)
        self.assertEqual(self.display.id, 1)
        self.assertEqual(self.display.message, "Welcome to the car park")
        self.assertEqual(self.display.is_on, True)
        self.assertIsInstance(self.display.car_park, CarPark)

    def test_update(self):
        self.display.update({"message": "Goodbye"})
        self.assertEqual(self.display.message, "Goodbye")

