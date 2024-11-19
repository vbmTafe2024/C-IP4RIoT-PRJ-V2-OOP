class CarPark:
    def __init__(self, location, capacity, plates=None, sensors=None, displays=None):
        self.location = location
        self.capacity = capacity
        self.plates = plates or []
        self.sensors = sensors or []
        self.displays = displays or []

    def __str__(self):

        return (f"CarPark Location: {self.location}, Capacity: {self.capacity}, "
                f"Available Bays: {self.capacity - len(self.plates)}, "
                f"Registered Cars: {len(self.plates)}, "
                f"Sensors: {len(self.sensors)}, Displays: {len(self.displays)}")

#tag