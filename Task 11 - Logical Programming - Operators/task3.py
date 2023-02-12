#store input and declare variables

swimming = int(input("Time in minutes for swimming:"))
cycling = int(input("Time in minutes for swimming:"))
running = int(input("Time in minutes for running:"))

# read in the time in minutes for all three events
# display total time to complete triathalon

total_time = swimming + cycling + running

# if statements to determine the award based on qualifying time

if total_time <= 100:
    print ("You have been awarded Provincial Colours")

elif (total_time <= 105) and (total_time >=100) :
    print("You have been awarded Provincial Half Colours")

elif (total_time <= 110) and (total_time >=105) :
    print("You have been awarded Provincial Scroll")

else:
    print("You have no award")