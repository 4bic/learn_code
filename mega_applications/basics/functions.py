def minutes_to_hours(minutes):
    hours = minutes / 60.00
    return hours

def seconds_to_hours(seconds):
    hours = seconds / 3600.00
    return hours

def mins_and_secs_to_hours(mins, secs):
    hours = mins / 60.00 + secs / 3600.00
    return hours


if __name__ == '__main__':
    print minutes_to_hours(120)
    print seconds_to_hours(1800)
    print mins_and_secs_to_hours(540, 3600)
