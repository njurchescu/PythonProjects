from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
RANDOM_POSITION = (random.randint(280, 1000), random.randint(-280, 280))


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = 5
        self.create_cars()
        self.move_cars()

    def create_cars(self):
        for i in range(25):
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(random.randint(280, 1000), random.randint(-240, 240))
            self.all_cars.append(car)

    def move_cars(self):
        for car in self.all_cars:
            car.back(self.STARTING_MOVE_DISTANCE)

    # def increase_speed(self):
    def reset_position(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                car.goto(random.randint(280, 1000), random.randint(-240, 240))

    def increase_speed(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.move_cars()

# Check if cars are too close to each other, if yes, increase distance with 10
