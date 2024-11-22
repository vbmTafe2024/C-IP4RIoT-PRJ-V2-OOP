import json
import unittest
from carPark import CarPark
from pathlib import Path

class TestCarPark(unittest.TestCase):

    def setUp(self):
        self.car_park = CarPark("123 Example Street", 100)
        self.log_file_name = "new_log.txt"
        self.log_file_path = Path(self.log_file_name)

    def tearDown(self):
        if self.log_file_path.exists():
            self.log_file_path.unlink(missing_ok=True)

    def test_car_park_initialized_with_all_attributes(self):
        self.assertIsInstance(self.car_park, CarPark)
        self.assertEqual(self.car_park.location, "123 Example Street")
        self.assertEqual(self.car_park.capacity, 100)
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.sensors, [])
        self.assertEqual(self.car_park.displays, [])
        self.assertEqual(self.car_park.available_bays, 100)
        self.assertEqual(self.car_park.log_file, Path("log.txt"))

    def test_log_file_created(self):
        new_carpark = CarPark("123 Example Street", 100, log_file=self.log_file_name)
        self.assertTrue(self.log_file_path.exists())

    def test_car_logged_when_entering(self):
        new_carpark = CarPark("123 Example Street", 100, log_file=self.log_file_name)
        new_carpark.add_car("FAKE-001")
        with new_carpark.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("FAKE-001", last_line)  # Check plate is logged
        self.assertIn("entered", last_line)  # Check entry type is logged
        self.assertIn("\n", last_line)       # Check newline exists

    def test_car_logged_when_exiting(self):
        new_carpark = CarPark("123 Example Street", 100, log_file=self.log_file_name)
        new_carpark.add_car("FAKE-001")
        new_carpark.remove_car("FAKE-001")
        with new_carpark.log_file.open() as f:
            last_line = f.readlines()[-1]
        self.assertIn("FAKE-001", last_line)  # Check plate is logged
        self.assertIn("exited", last_line)   # Check exit type is logged
        self.assertIn("\n", last_line)       # Check newline exists

    def test_add_car(self):
        self.car_park.add_car("FAKE-001")
        self.assertEqual(self.car_park.plates, ["FAKE-001"])
        self.assertEqual(self.car_park.available_bays, 99)

    def test_remove_car(self):
        self.car_park.add_car("FAKE-001")
        self.car_park.remove_car("FAKE-001")
        self.assertEqual(self.car_park.plates, [])
        self.assertEqual(self.car_park.available_bays, 100)

    def test_overfill_the_car_park(self):
        for i in range(100):
            self.car_park.add_car(f"FAKE-{i}")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.add_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)
        self.car_park.remove_car("FAKE-100")
        self.assertEqual(self.car_park.available_bays, 0)

    def test_removing_a_car_that_does_not_exist(self):
        with self.assertRaises(ValueError):
            self.car_park.remove_car("NO-1")

    def test_register_raises_type_error(self):
        with self.assertRaises(TypeError):
            self.car_park.register("Not a Sensor or Display")

    def test_write_config(self):
        self.car_park.write_config()
        with open("config.json") as f:
            config = json.load(f)
        self.assertEqual(config["location"], self.car_park.location)
        self.assertEqual(config["capacity"], self.car_park.capacity)
        self.assertEqual(config["log_file"], str(self.car_park.log_file))

    def test_from_config(self):
        self.car_park.write_config()
        loaded_car_park = CarPark.from_config()
        self.assertEqual(loaded_car_park.location, self.car_park.location)
        self.assertEqual(loaded_car_park.capacity, self.car_park.capacity)
        self.assertEqual(loaded_car_park.log_file, self.car_park.log_file)


if __name__ == "__main__":
    unittest.main()
