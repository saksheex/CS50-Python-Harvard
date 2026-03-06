def main():

    time = input("What time is it?: ").casefold()
    time = convert(time)
    if 7 <= time <=8 :
       print("Breakfast Time")
    elif 12 <= time <=13 :
        print("Lunch Time")
    elif 18 <= time <= 19 :
        print("Dinner Time")  
    else:
        print("No time for meal")     


def convert(time):

    time,period = time.split()
    hours , minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    if period == "am":
        if hours == 12:
            hours = 0
    elif period == "pm":
         if hours != 12:
             hours = hours+12
    return hours + minutes / 60     
    
if __name__ == "__main__":
     main()
