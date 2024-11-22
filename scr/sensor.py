from abc import ABC, abstractmethod
import random


class Sensor(ABC):  # inherit from ABC
    def __init__(self, id, is_active, car_park):
        self.id = id
        self.is_active = is_active
        self.car_park = car_park

    @abstractmethod
    def update_car_park(self, plate):
        pass

    def _scan_plate(self):
        # Generate a random plate for simulation
        return 'FAKE-' + format(random.randint(0, 999), "03d")

    def detect_vehicle(self):
        plate = self._scan_plate()
        self.update_car_park(plate)

    def __str__(self):
        status = "Active" if self.is_active else "Inactive"
        return f"Sensor {self.id}: {status}"


class TemperatureSensor(Sensor):
    def __init__(self, id, is_active, car_park, temperature=22):
        super().__init__(id, is_active, car_park)
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature


class EntrySensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.add_car(plate)
        print(f"Incoming 🚘 vehicle detected. Plate: {plate}") # emoji copied from the instructions of GitHub car park


class ExitSensor(Sensor):
    def update_car_park(self, plate):
        self.car_park.remove_car(plate)
        print(f"Outgoing 🚗 vehicle detected. Plate: {plate}")  # emoji copied from the instructions of GitHub car park

    def _scan_plate(self):
        # Randomly select an existing plate from the car park for simulation
        if self.car_park.plates:
            return random.choice(self.car_park.plates)
        else:
            print("No vehicles in the car park to scan.")
            return None