from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
NUMBER_OF_CARS = 20
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self) -> None:
        self.move_speed = STARTING_MOVE_DISTANCE
        self.cars = []
        for _ in range(NUMBER_OF_CARS):
            car = Turtle()
            rand_x = random.randint(-320, 320)
            rand_y = random.randint(-260, 260)
            car.penup()
            car.shape('square')
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(rand_x, rand_y)
            car.setheading(180)
            self.cars.append(car)
    
    def move_cars(self):
        for car in self.cars:
            car.forward(self.move_speed)
            if car.xcor() < -320:
                rand_y = random.randint(-260, 260)
                car.color(random.choice(COLORS))
                car.goto(320, rand_y)
    
    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT
        