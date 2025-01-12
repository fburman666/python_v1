distance = 470 #km
speed = input ("hur fort kör du (angett i km/h)? ")
speed_si = float(speed)/3.6
time = 1000 * distance/speed_si
print("Det tar " + str(time) + " sekunder att köra sträckan sthlm - gbg")
time_minutes = 1000 * distance/speed_si/60
print("Det tar " + str(time_minutes) + " minuter att köra sträckan sthlm - gbg")
time_hrs = 1000 * distance/speed_si/3600
time_fullhrs = 1000 * distance/speed_si//3600
time_minutes = 1000 * distance/speed_si/60
time_fullminutes = time_minutes % 60
print("det tar " + str(time_hrs) + "att köra")
print("Det tar " + str(time_fullhrs) +"h " +str(time_fullminutes) + "min att köra sträckan sthlm - gbg")