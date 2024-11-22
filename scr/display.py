class Display:
    def __init__(self, id, car_park, message="", is_on=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message if self.message else 'No message'}"

    def update(self, data):
        # Update the display's message if the data contains a 'message' key - fixing the test failure
        if "message" in data:
            self.message = data["message"]

        # Print all key-value pairs from the data for logging
        for key, value in data.items():
            print(f"{key}: {value}")