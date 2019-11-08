#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()
choice = "y"
while choice.lower() == "y":
    print()
    miles_driven = float(input("Enter miles driven:\t\t"))
    gallons_used = float(input("Enter gallons of gas used:\t\t"))
    cost_per_gallon = float(input("Enter cost per gallon:\t\t")
    print()
    mpg = (miles_driven / gallons_used, 2)
    tgc = round(mpg, 2)
    cpm = round(tcp / miles_drivers, 1)         
    print("Miles Per Gallon:\t\t" + str(mpg))
    print("total gas cost:\t\t\t" + str(tgc))
    print("cost per mile:\t\t\t" + str(cpm))
    print()
    choice = input("Get entries for another trip?" (y/n): ")
print() 
print("bye")

