hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

hour = hour + mins

mins = mins + dura

mins = mins % 60 

hour = hour % 24

print(hour, ":", mins, sep='')

