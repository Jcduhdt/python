cars = 100#车有100辆
space_in_a_car = 4.0#每辆车最多能坐4人，装4个乘客
drivers = 30#有30个司机
passengers = 90#有90个乘客
cars_not_driven = cars - drivers#剩下没开走的车=车数-司机数
cars_driven = drivers#能被开走的车的数目=司机数
carpool_capacity = cars_driven * space_in_a_car#拼车容量（总共可载走人数）=可开走的车数*车的最大容纳空间
average_passengers_per_car = passengers / cars_driven#平均每辆车乘客数=总人数/可被开走的车数


print("There are", cars, "cars available")#输出这里有几辆车
print("There are only", drivers, "drivers available")#输出这里只能开走多少辆车
print("There will be", cars_not_driven, "empty cars today")#输出将会有多少辆不能被开走的车
print("We can transport", carpool_capacity, "people today")#我们今天可以载走多少人
print("We have", passengers, "to carpool today")#今天有多少乘客来坐车
print("We need to put about", average_passengers_per_car, "in each car.")#我们需要每辆车装多少乘客
