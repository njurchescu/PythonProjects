import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()

cars_manager = CarManager()

screen.listen()
screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    # Make cars move
    cars_manager.move_cars()
    # Check if the cars reached end of x-axis and re-position them
    cars_manager.reset_position()

    # Check collision with cars
    for car in cars_manager.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_finished()
            game_is_on = False

    # Detect if player reached finish line and increase level and cars speed
    if player.finish():
        scoreboard.increase_level()
        cars_manager.increase_speed()

screen.exitonclick()
