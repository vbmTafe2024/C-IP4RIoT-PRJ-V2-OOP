def test_register_raises_type_error(self):
    with self.assertRaises(TypeError):
        self.car_park.register("Not a Sensor or Display")