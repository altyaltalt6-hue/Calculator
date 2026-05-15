print("Welcome to my calculator! I made this for my physics class")

#this is the main loop for the calculator
while True:
    #this input lets the user decide which calculator they want to use
    use = input("What would you like to use?\nForce calculator,\nspeed calculator,\ndistance calculator,\n mass calculator,\n ")
    #I used a try/except thing here to stop the calculator from crashing if you input something that isn't a number
    try:
        #this is the force calculator
        if use.lower() == "force":
            #these are the values of the object
            mass = int(input("Please input mass\n"))
            acceleration = int(input("Please input acceleration\n"))
            #this does the calculation and tells the user what calculation was used
            print("Now we multiply mass and acceleration! {} x {} = {}".format(mass, acceleration, (mass*acceleration)))
        #this is the speed calculator
        elif use.lower() == "speed":
            #these are the values of the object
            distance = int(input("Please input the distance\n"))
            time = int(input("Please input the time your object travelled for\n"))
            #this does the calculation and tells the user what calculation was used
            print("Now we divide distance by time! {}/{} = {}".format(distance, time, (distance/time)))
        #this is the mass calculator
        elif use.lower() == "mass":
            #these are the values of the object
            acceleration = int(input("Please enter the acceleration\n"))
            force = int(input("Please enter the force\n"))
            #this does the calculation and tells the user what calculation was used
            print("Now we divide force by acceleration! {}/{} = {}".format(force, acceleration, (force/acceleration)))
        #this is the distance calculator
        elif use.lower() == "distance":
            #these are the object values
            velocity = int(input("Please enter the velocity/speed\n"))
            time = int(input("Please enter the time your object was travelling for\n"))
            #this does the calculation and tells the user what calculation was used
            print("Now we multiply velocity by time! {} x {} = {}".format(velocity, time, (velocity * time)))
    #this ignores invalid inputs (E.G letter in the integer inputs) and tells the user the input is invalid. code loops back to start
    except(ValueError):
        print("Invalid input, try using a number!")