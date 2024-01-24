import time

print(time.ctime(0)) #time expressed in seconds since epoch to a readable string. epoch is when the computer was made, idk

# timestamp = 5:33:39

time_object = time.localtime() # local time
print(time_object)
#--or--
time_object = time.gmtime() # UTC time
local_time = time.strftime("%B %d %Y %H:%M:%S", time_object)
# .strftime takes a format input, and a time object.
# look up python's time access and conversion table for more percentage character items
# month day year hour minute second


# this function here takes a string of time and makes it a time object
time_string = "20 April, 2020"
time_object = time.strptime(time_string,"%d %B, %Y")
print(time_object)
