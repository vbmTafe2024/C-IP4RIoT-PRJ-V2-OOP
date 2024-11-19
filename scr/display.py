class Display:
    def __init__(self, id, car_park, message="", is_on=False):
        self.id = id
        self.car_park = car_park
        self.message = message
        self.is_on = is_on

    def __str__(self):
        return f"Display {self.id}: {self.message if self.message else 'No message'}"

    def update(self, data):

        for key, value in data.items():
            print(f"{key}: {value}")