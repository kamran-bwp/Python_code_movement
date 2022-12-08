#3.1 Drivers are concerned with the mileage obtained by their automobiles. One driver
#has kept track of several tankfuls of gasoline by recording miles driven and gallons used
#for each tankful. Develop a Python program that prompts the user to input the miles
#driven and gallons used for each tank- ful. The program should calculate and display the
#miles per gallon obtained for each tankful. After processing all input information, the
#program should calculate and print the combined miles per gal- lon obtained for all
#tankful (= total miles driven divided by total gallons used).
#Enter the gallons used (-1 to end): 12.8
#Enter the miles driven: 287
#The miles / gallon for this tank was 22.421875
#Enter the gallons used (-1 to end): 10.3
#Enter the miles driven: 200
#The miles / gallon for this tank was 19.417475
#Enter the gallons used (-1 to end): 5
#Enter the miles driven: 120
#The miles / gallon for this tank was 24.000000
#Enter the gallons used (-1 to end): -1
#The overall average miles/gallon was 21.601423

total_gallons = 0
total_miles = 0
gall = float(input("Enter the gallons used(-1 to end): "))
while gall > 0:
    milesDriven = float(input("Enter the miles driven: "))
    average_consumption = milesDriven/gall
    total_miles = total_miles + milesDriven
    total_gallons = total_gallons + gall
    print(f"The miles / gallon for this tank was {average_consumption}")
    gall = float(input("Enter the gallons used(-1 to end): "))

if gall > 0:
    print(f"The overall average miles/gallon was {total_miles/total_gallons}")
else:
    print("Nothing entered")
