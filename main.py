import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard, FONT

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
game_is_on = True
screen.tracer(0)
screen.listen()
screen.onkeypress(player.move, "Up")
sleep_time = 0.1
while game_is_on:
    time.sleep(sleep_time)
    screen.update()
    car_manager.gen_new_cars()
    car_manager.move_cars()
    if player.ycor() >= 280:
        scoreboard.update_score()
        player.res()
        # On increasing level we will increase speed of the cars by
        # reducing delay in time or calling level_up
        # car_manager.level_up()
        sleep_time *= 0.5

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            player.write("GAME OVER", font=FONT)
            game_is_on = False
            break

screen.exitonclick()
