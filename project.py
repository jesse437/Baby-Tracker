import csv
import os
from datetime import datetime

def main():
    """Runs baby tracker program"""
    print("Baby Tracker")
    
    while True:
        date = input("Enter today's date (YYYY-MM-DD): ")
        date_object = validate_date(date)
        if date_object:
            print("Today is:", date_object.strftime("%B %d, %Y"))
            break
        else:
            print("Invalid Entry")
            
    while True:
        
        print("a. sleep_start")
        print("b. sleep_end")
        print("c. feed")
        print("d. diaper")
        print("e. burp")
        print("f. view log")
        print("g. quit")
        
        activity = input("Enter selection: ").lower()
        
        
        if activity == "a":
            if log_event("sleep_start"):
                print("Logged: sleep_start")
        elif activity == "b":
            if log_event("sleep_end"):
                print("Logged: sleep_end")
        elif activity == "c":
            if log_event("feed"):
                print("Logged: fed")
        elif activity == "d":
            if log_event("diaper"):
                print("Logged: diaper changed")
        elif activity == "e":
            if log_event("burp"):
                print("Logged: burp")
        elif activity == "f":
            view_log()
        elif activity == "g":
            print("Goodbye!")
            break
        else:
            print("Invalid entry")
            
def validate_date(date):
    """Return a datetime object if date is valid YYYY-MM-DD, otherwise None."""
    try:
        return datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return None
        

def log_event(event, filename="baby_log.csv"):
    """Append one timestamped event to the log CSV."""
    time = datetime.now().strftime("%Y-%m-%d %H:%M")
    file_exists = os.path.exists(filename)
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=["time", "event"])
        if not file_exists:
            writer.writeheader()
        writer.writerow({"time":time, "event": event})
    return True
    

def view_log(filename="baby_log.csv"):
    """Print every logged event, or a message if the log doesn't exist yet."""
    if not os.path.exists(filename):
        print("No logs yet")
        return
        
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"time: {row['time']} - {row['event']}")
    
            

if __name__ == "__main__":
    main()