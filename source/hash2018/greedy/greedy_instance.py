from hash2018.reader import *
from hash2018.writer import *
from hash2018.utility import *
from hash2018.simplesolution import *


global_time = 0
problem = EXAMPLE
data = read_in(problem)
rides = data[DATA]
cars = [Car()] * data[FLEET]

solution = []
for car in cars:
    car_solution, rides,  = schedule_car(posstart=car.loc,
                                          tsstart=global_time,
                                          avrides=rides,
                                          bonus=data[BONUS])
    solution.append(car_solution)

rides_for_car = []
for sol in solution:
    rides_for_car.append([i[0] for i in solution])


print(rides_for_car)
