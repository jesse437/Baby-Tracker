import csv
import os
from datetime import datetime

def main():
    
    print("Baby Tracker")
    
    while True:
        
        try:
            date = input("Enter today's date (YYYY-MM-DD): ")
            date_object = datetime.strptime(date, "%Y-%m-%d")
            print("You entered:", date_object.strftime("%B %d, %Y"))
            break
                
        except ValueError:
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
            log_event("sleep_start")
        elif activity == "b":
            log_event("sleep_end")
        elif activity == "c":
            log_event("feed")
        elif activity == "d":
            log_event("diaper")
        elif activity == "e":
            log_event("burp")
        elif activity == "f":
            view_log()
        elif activity == "g":
            print("quit")
            break
        else:
            print("Invalid entry")
        

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
    if not os.path.exists(filename):
        print("No logs yet")
        return
        
    with open(filename) as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(f"time: {row['time']} - {row['event']}")
            
        
            
        
    
    

if __name__ == "__main__":
    main()