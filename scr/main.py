from carPark import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display


# Simulating entry
def simulate_entry(sensor, plate):
    if sensor.is_active:
        sensor.car_park.add_car(plate)
        print(f"Car {plate} entered through the entry sensor.")
    else:
        print("Entry sensor is inactive.")


# Simulating exit
def simulate_exit(sensor, plate):
    if sensor.is_active:
        try:
            sensor.car_park.remove_car(plate)
            print(f"Car {plate} exited through the exit sensor.")
        except ValueError:
            print(f"Car {plate} not found in the car park.")
    else:
        print("Exit sensor is inactive.")


# TODO: Create a car park object with the location 'Moondalup', capacity 100, and log_file "moondalup.txt"
car_park = CarPark("Moondalup", 100, log_file="moondalup.txt")

# TODO: Create an entry sensor object with id 1, is_active True, and car_park car_park
entry_sensor = EntrySensor(1, True, car_park)

# TODO: Create an exit sensor object with id 2, is_active True, and car_park car_park
exit_sensor = ExitSensor(2, True, car_park)

# TODO: Create a display object with id 1, message "Welcome to Moondalup", is_on True, and car_park car_park
display = Display(1, "Welcome to Moondalup", True, car_park)

# TODO: Drive 10 cars into the car park (must be triggered via the sensor - NOT by calling car_park.add_car directly)
for cars_coming in range(10):
    plate = f"CAR-{cars_coming:03d}"  # Generate plates like CAR-000, CAR-001...
    simulate_entry(entry_sensor, plate)

# TODO: Drive 2 cars out of the car park (must be triggered via the sensor)
for cars_leaving in range(2):
    plate = f"CAR-{cars_leaving:03d}"  # Reuse the plates of cars that entered
    simulate_exit(exit_sensor, plate)
