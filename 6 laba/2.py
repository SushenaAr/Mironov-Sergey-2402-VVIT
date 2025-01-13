class Vehicle:
    def __init__(self, make, model, v):
        self.make = make
        self.model = model
        self.v = v

    def get_info(self):
        return self.make, self.model

    def get_v(self):
        return self.v


class Car(Vehicle):
    def __init__(self, make, model, v, fuel_type):
        super().__init__(make, model, v)
        self.fuel_type = fuel_type

    def get_info(self):
        return self.make, self.model, self.fuel_type

    def test(self):
	return "ok"



if __name__ == '__main__':
    car = Car('Lorem', 'Ipsum', 25, '95')
    print(car.get_v())
    print(car.test())
    print(car.get_info())