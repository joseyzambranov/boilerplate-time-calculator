def add_time(start, duration , start_day=False):

    duration_part = duration.partition(":")
    start_part = start.partition(":")

    duration_hour = int(duration_part[0])
    duration_min = int(duration_part[2])
    
    start_min_part = start_part[2].partition(" ")
    start_hour = int(start_part[0])
    start_min = int(start_min_part[0])

    am_or_pm = start_min_part[2]
    
    amount_of_days = int(duration_hour / 24)

    total_hour = duration_hour + start_hour
    total_min = duration_min + start_min

    if(total_min>=60):
        total_hour +=1
        total_min = total_min % 60

    print(
        {
            "start_part":start_part,
            "duration_part":duration_part,
            "start_hour":start_hour,
            "start_min":start_min,
            "duration_hour":duration_hour,
            "duration_min":duration_min,
            "am_or_pm":am_or_pm,
            "amount_of_days":amount_of_days,
            "total_hour":total_hour,
            "total_min":total_min
        }
        )

    return "The End"