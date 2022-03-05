from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class NewCar(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        # self.hideturtle()
        self.penup()
        self.color(random.choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)


class CarManager():
    def __init__(self):
        super().__init__()
        self.car_speed=STARTING_MOVE_DISTANCE
        self.all_cars = []

    def gen_new_cars(self):
        cars_should_be_generated= random.randint(1, 6)
        if cars_should_be_generated==1:
            newcar = NewCar()
            newcar.goto(300, random.randint(-240, 250))
            self.all_cars.append(newcar)

    def move_cars(self):
        for car in self.all_cars:
            car.bk(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
