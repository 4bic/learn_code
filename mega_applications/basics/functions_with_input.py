def mins_secs_hours_converter():
    converter = input("Select 1 to change minutes to hours or 2 for seconds to hours : ")

    if converter is 1:
        minutes = input("Enter no of minutes to be converted:  ")
        def minutes_to_hours(minutes):
            hours = minutes / 60.00
            return float(hours)
        print 'That amounts to',minutes_to_hours(minutes), 'Hours'

    elif converter is 2:
        seconds = input("Enter no of seconds to be converted:  ")
        def seconds_to_hours(seconds):
            hours = seconds / 3600.00
            return float(hours)
        print 'That amounts to',seconds_to_hours(seconds), 'Hours'

    else:
        print "Invalid choice ! please enter either 1 or 2"
    return mins_secs_hours_converter()

if __name__ == '__main__':
    mins_secs_hours_converter()
