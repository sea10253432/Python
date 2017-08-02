# _*_ coding: utf-8 _*_

# 汽车数量
cars =  100
# 每辆车上的座位数量
space_in_a_car = 4.0
# 司机数量
drivers = 30
# 乘客数量
passengers = 90
# 没有司机的车辆
cars_not_driven = cars - drivers
# 有司机的车辆
cars_driven = drivers
# 最大载客量
carpool_capacity = cars_driven * space_in_a_car
# 平均每辆车上的乘客数量
average_passengers_per_car = passengers / cars_driven


print "Ther are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven,"empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

