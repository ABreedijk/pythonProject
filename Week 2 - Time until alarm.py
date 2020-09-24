current_time_str = input("What is the current time in hours (0-23)?")
wait_time_str = input("How many hours do you want to wait?")
current_time = int(current_time_str)
wait_time = int(wait_time_str)
alarm = (current_time + wait_time)%24
print("The time after waiting is:", alarm)
