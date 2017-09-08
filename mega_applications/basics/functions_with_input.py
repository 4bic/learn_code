def minutes_to_hours(minutes):
    hours = minutes / 60.00
    return float(hours)

def seconds_to_hours(seconds):
    hours = seconds / 3600.00
    return float(hours)

def mins_secs_hours_converter():
    converter = input("Select 1 to change minutes to hours or 2 for seconds to hours : ")

    if converter is 1:
        minutes = input("Enter no of minutes to be converted:  ")
        print 'That amounts to',minutes_to_hours(minutes), 'Hours'

    elif converter is 2:
        seconds = input("Enter no of seconds to be converted:  ")
        print 'That amounts to',seconds_to_hours(seconds), 'Hours'
    else:
        print "Invalid choice ! please enter either 1 or 2"

if __name__ == '__main__':
    mins_secs_hours_converter()
