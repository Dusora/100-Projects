print ("Welcome to the tip calculator.")
 
Bill= float(input("What was the total bill? "))
People= int(input("How many people? "))
percent= int(input("What percentage tip would you like to give? 10, 12, or 15? "))
tip_percent= percent/100
total_tip= Bill*tip_percent
total=Bill+total_tip
split=total/People
final= round(split, 2)
final= "{:.2f}". format(split)
print("Each person should pay: " ,final)

