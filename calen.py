import calendar
import os
import sys

def calen():
    os.system("cls")

    print("Welcome to the calendar viewer")
    print()

    calendar.setfirstweekday(calendar.SUNDAY)

    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))

    if year < 1 :
        print("Please enter a valid year number eg. 2008")
    elif month < 1 or month > 12:
        print("Please enter a valid month number between 1 and 12")
    else:
        print()
        x = calendar.month(year,month)
        print(x)

        os.system("pause")

        choice_section()

def choice_section():
    os.system("cls")

    print("=" * 40)
    print("[1] View Calendar")
    print("[2] Exit")
    print("=" * 40)

    choice = input("Enter your choice: ")

    if choice == "1":
        calen()
    elif choice == "2":
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        os.system("pause")
        choice_section()

calen()