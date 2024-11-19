from sensor import Sensor, TemperatureSensor
from display import Display


class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

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

    def remove_car(self, plate):
        if plate in self.plates:
            self.plates.remove(plate)
            self.update_displays()
        else:
            print("Car plate not found in the car park.")

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
