def add_time(start, duration , day_of_week=False):

    def extract_time(time_str):
        hour, minute, period = map(str.strip, time_str.replace(":", " ").split())
        return int(hour), int(minute), period
    
    def extract_time_duration(time_str):
        hour, minute = map(str.strip, time_str.replace(":", " ").split())
        return int(hour), int(minute)
    
    def calculate_total_min(start_min, duration_min,start_hour):
        total_min = duration_min + start_min
        final_start_hour = start_hour
        if(total_min>=60):
            final_start_hour +=1
            total_min = total_min % 60
        total_min = total_min if total_min >=10 else "0" + str(total_min)    
        return total_min ,final_start_hour
    
    def calculate_total_hour(duration_hour,final_start_hour):
        total_hour = duration_hour + final_start_hour
        total_hour = int((final_start_hour + duration_hour) % 12) 
        total_hour = total_hour = 12 if total_hour == 0 else total_hour  
        return total_hour
    
    def calculate_am_or_pm(final_start_hour,duration_hour,am_or_pm):
        am_pm_obj = {"AM":"PM","PM":"AM"}
        amount_of_days = int(duration_hour / 24)
        change_am_pm = int((final_start_hour + duration_hour) / 12)
        if (am_or_pm == "PM" and final_start_hour + (duration_hour % 12) >= 12):
            amount_of_days += 1 
        final_am_or_pm = am_pm_obj[am_or_pm] if change_am_pm % 2 == 1 else am_or_pm
        return final_am_or_pm , amount_of_days
    
    def calculate_result_time(total_hour,total_min,final_am_or_pm,day_of_week,amount_of_days):
        days_of_the_week_index = {"monday": 0, "tuesday": 1, "wednesday": 2, "thursday": 3, "friday": 4, "saturday": 5, "sunday": 6}
        days_of_the_week_array = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return_time = return_time = f"{total_hour}:{total_min} {final_am_or_pm}"
        if(day_of_week):
          day_of_week = day_of_week.lower()
          index = int((days_of_the_week_index[day_of_week]) + amount_of_days) % 7
          new_day = days_of_the_week_array[index]
          return_time += ", " + new_day

        if(amount_of_days == 1):
          return return_time + " " + "(next day)"
        elif(amount_of_days > 1):
          return return_time + " (" + str(amount_of_days) + " days later)"   
        return return_time
        
    start_hour, start_min, am_or_pm = extract_time(start)
    duration_hour, duration_min = extract_time_duration(duration)
    total_min , final_start_hour = calculate_total_min( start_min, duration_min,start_hour)
    total_hour = calculate_total_hour(duration_hour,final_start_hour)
    final_am_or_pm , amount_of_days = calculate_am_or_pm(final_start_hour , duration_hour,am_or_pm)
    result_time = calculate_result_time(total_hour,total_min,final_am_or_pm,day_of_week,amount_of_days)

    return result_time
