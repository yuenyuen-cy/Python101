import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Turtle Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.player_move, "Up")


game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Move cars
    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with cars
    for car in car_manager.cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect when player reach top of finish line
    if player.ycor() > 280:
        scoreboard.level_up()
        player.reset_position()
        car_manager.increase_speed()



screen.exitonclick()