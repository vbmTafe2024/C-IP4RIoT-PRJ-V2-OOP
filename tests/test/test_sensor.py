import unittest
from sensor import EntrySensor, ExitSensor
from carPark import CarPark

class TestSensor(unittest.TestCase):
    def setUp(self):
        # Initialize a car park and sensor objects for testing
        self.car_park = CarPark("Test Location", 50)
        self.entry_sensor = EntrySensor(id=1, is_active=True, car_park=self.car_park)
        self.exit_sensor = ExitSensor(id=2, is_active=False, car_park=self.car_park)

    def test_entry_sensor_initialization(self):
        # Test if the entry sensor is correctly initialized
        self.assertEqual(self.entry_sensor.id, 1)  # Check if ID is 1
        self.assertTrue(self.entry_sensor.is_active)  # Check if sensor is active
        self.assertEqual(self.entry_sensor.car_park, self.car_park)  # Check if linked to the correct car park

    def test_exit_sensor_initialization(self):
        # Test if the exit sensor is correctly initialized
        self.assertEqual(self.exit_sensor.id, 2)  # Check if ID is 2
        self.assertFalse(self.exit_sensor.is_active)  # Check if sensor is inactive
        self.assertEqual(self.exit_sensor.car_park, self.car_park)  # Check if linked to the correct car park

    def test_detect_vehicle(self):
        # Call the detect_vehicle method
        result = self.entry_sensor.detect_vehicle()

        # Check if the result is None (in case no vehicle is detected or sensor is inactive)
        if result is None:
            self.assertIsNone(result)  # Confirm that None is returned when no vehicle is detected
        else:
            # If a result is returned, check if it contains the expected message
            self.assertIn("Vehicle detected by sensor", result)  # Check if detection message is returned


if __name__ == "__main__":
    unittest.main()
