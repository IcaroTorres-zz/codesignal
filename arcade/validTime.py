# Check if the given string is a correct time representation of the 24-hour clock.

def validTime(time):
    time = time.split(':') # split ':'. len==2
    #
    if len(time)==2 and 0<= int(time[0]) <=23 and 0<= int(time[1]) <= 59:
        return True # list [int(valid hour string),int(valid minute string)]
    else:
        return False # if len !=2 or some invalid value inside
