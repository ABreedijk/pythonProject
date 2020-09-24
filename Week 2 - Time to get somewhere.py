distance_str = input('How far do you need to go (in km)?')
distance = int(distance_str)

speed_walk = int(input('How fast do you walk on average (in km/h)?'))
speed_bike = int(input('How fast do you ride your bike on average (in km/h)?'))
speed_car = int(input('How fast do you drive your car on average (in km/h)?'))

time_walk_hour = distance // speed_walk
time_walk_min = (distance % speed_walk) // (speed_walk/60)

time_bike_hour = distance // speed_bike
time_bike_min = (distance % speed_bike) // (speed_bike/60)

time_car_hour = distance // speed_car
time_car_min = (distance % speed_car) // (speed_car/60)

print('By walking: ', time_walk_hour, 'hours and',time_walk_min, 'minutes')
print('By biking: ', time_bike_hour, 'hours and',time_bike_min, 'minutes')
print('By driving: ', time_car_hour, 'hours and', time_car_min, 'minutes')



