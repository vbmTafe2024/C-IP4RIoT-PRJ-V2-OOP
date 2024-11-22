from sensor import Sensor, TemperatureSensor
from pathlib import Path
from datetime import datetime # we'll use this to timestamp entries
from display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None, log_file=Path("log.txt")):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []
        self.log_file = log_file if isinstance(log_file, Path) else Path(log_file)
        self.log_file.touch(exist_ok=True)  # Create the log file if it doesn't exist

    def __str__(self):
        return f"Car Park at {self.location}, Capacity: {self.capacity}"

    def register(self, component):

        if not isinstance(component, (Sensor, Display)):
            raise TypeError("Object must be a Sensor or Display")

        if isinstance(component, Sensor):
            self.sensors.append(component)
        elif isinstance(component, Display):
            self.displays.append(component)

    @property
    def available_bays(self):
        # Return 0 if the number of cars exceeds capacity
        return max(self.capacity - len(self.plates), 0)

    def add_car(self, plate):
        self.plates.append(plate)  # Always add the car, no full capacity
        self.update_displays()
        self._log_car_activity(plate, "entered")

    def remove_car(self, plate):
        if plate not in self.plates:
            raise ValueError("Car plate not found in the car park.")
        self.plates.remove(plate)
        # No need to update available_bays directly because it's computed dynamically - fixing test failure
        self.update_displays()
        self._log_car_activity(plate, "exited")  # Log the car's exit

    def update_displays(self):
        # Build the data dictionary to send to displays
        data = {
            "available_bays": self.available_bays,
            "temperature": self.get_temperature(),
            "time": self.get_time()
        }

        # Send the data to all displays
        for display in self.displays:
            display.update(data)

    def get_temperature(self):
        # getting the temperature from a sensor
        for sensor in self.sensors:
            if isinstance(sensor, TemperatureSensor) and sensor.is_active:
                return sensor.get_temperature()

    def get_time(self):
        # getting the current time
        import time
        return time.strftime("%H:%M:%S")

    def _log_car_activity(self, plate, action):
        with self.log_file.open("a") as f:
            f.write(f"{plate} {action} at {datetime.now()}\n")
