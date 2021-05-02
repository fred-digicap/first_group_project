# this imports the datetime module to enable us use date and time in our program
from datetime import datetime

from datetime import timedelta

import csv # Imports the csv library contains objects and other code to read, write, and process data from and to CSV files

def main():


    print("\nHi cherished employee.\n")

    print("\nKindly choose a number:" #'\n' indents the text that follows it
          "\n 1. Start timer"
          "\n 2. Check wages for current task"
          "\n 3. Exit program")
    selection = int(input())

    if selection == 1:
        start_time = datetime.now()
        print(start_time.strftime("\nStarting time is : %X"))
        print(start_time.strftime("\nTime : %H:%M"))
        print("Kindly enter  a number to stop the timer")
        stop = int(input())
        end_time = datetime.now()
        print(end_time.strftime("\nEnding time is : %X"))
        print(end_time.strftime("\nTime : %H:%M)"))
        # time difference calculation
        t = (end_time - start_time)
        secs = t.seconds
        minutes = ((secs/60)%60)/60.0
        hours = secs/3600
        total_hours = round(hours + minutes, 2)
        # wage calculation (difference *5, result in $)
        employee_wage = total_hours*5
        # add append to file
        with open('employee_wages.csv', 'a') as newFile: #Allows writing to the csv file specified
            newFileWriter = csv.writer(newFile)
            #The writerow() method writes a row of data into a specified file
            newFileWriter.writerow(['Start date', 'Start time', 'End date', 'End time ', 'Total hour ', 'Pay'])
            newFileWriter.writerow([start_time.strftime("%x"), start_time.strftime("%H:%M%p"), end_time.strftime("%x"), end_time.strftime("%H:%M%p"), total_hours, f"$ {employee_wage}"])
            # "%H:%M%p" creates indent in the excel file
        print("This work session was successfully added\n\n")
        print("\n%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n")
        main()
    elif selection == 2:
        print("\nKindly check your file named 'employee_wages.csv' for your wages for your current task. Thank you.")
        main()
    elif selection == 3:
        print("\nThanks for using this program. See you soon.")
        exit()
    else:
        print('\nSorry, you entered and invalid selection. Kindly try again.')
        main()

if __name__ == "__main__":
        main()