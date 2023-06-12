def add(*args):
    # args[0]
    sum_num = 0
    for n in args:
        sum_num += n
    return sum_num


print(add(3, 4, 5, 6, 3, 4, 5))


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:

    def __init__(self, **kwargs):
         self.make = kwargs.get("make")
         self.model = kwargs.get("model")
         self.color = kwargs.get("color")

mu_car = Car(make="Nissan")
print(mu_car.model)
