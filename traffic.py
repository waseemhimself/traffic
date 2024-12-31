import numpy as np


#Storing possible timers in a list to pick from later
timers = [30,40,50,60,70,80,90,100]


def evaporation_cars(car_count, timer, num_lanes):
    #Calculating the new count of cars that are on the road
    rate = 0.51
    throughput = int(timer * rate * num_lanes)

    return min(throughput,int(car_count))


def calculate_timer(car_count, num_lanes):
    #Calculating the timer needed for a road to maximise efficiency. Pick timer required from the timers list.
    if car_count <= 15 * num_lanes:
        return timers[0]
    elif 15 * num_lanes < car_count <= 20 * num_lanes:
        return timers[1]
    elif 20 * num_lanes < car_count <= 25 * num_lanes: 
        return timers[2]   
    elif 25 * num_lanes < car_count <= 30 * num_lanes:
        return timers[3]
    elif 30 * num_lanes < car_count <= 35 * num_lanes:
        return timers[4]
    elif 35 * num_lanes < car_count <= 40 * num_lanes:
        return timers[5]
    elif 40 * num_lanes < car_count <= 45 * num_lanes:
        return timers[6]
    else:
        return timers[7]


def calculate_throughput(car_count, timer_needed, num_lanes):
    #Calculating the count of cars that leave the road
    throughput1 = evaporation_cars(2/3*(car_count), timer_needed, num_lanes)

    return throughput1


def display_cars(type):
    #Displaying the count of cars that are present on each road
    if type == "T":
        print(f"Number of cars in south road in T-Intersection: {south_car_count_T}\n"
                f"Number of cars in east road in T-Intersection: {east_car_count_T}\n"
                f"Number of cars in west road in T-Intersection: {west_car_count_T}\n")
    
    elif type == "Plus":
        print(f"Number of cars in north road in Plus-Intersection: {north_car_count_Plus}\n"
                f"Number of cars in south road in Plus-Intersection: {south_car_count_Plus}\n"
                f"Number of cars in east road in Plus-Intersection: {east_car_count_Plus}\n"
                f"Number of cars in west road in Plus-Intersection: {west_car_count_Plus}\n")
        
    else:
        print("Display car count call error.")



#Initialising car counts on each road
south_car_count_T = np.random.randint(30,120)
east_car_count_T = np.random.randint(30,120)
west_car_count_T = np.random.randint(30,120)

north_car_count_Plus = np.random.randint(30,120)
south_car_count_Plus = np.random.randint(30,120)
east_car_count_Plus = np.random.randint(30,120)
west_car_count_Plus = np.random.randint(30,120)


#Storing all car counts in list to iterate over when needed
T_car_counts = ["south_car_count_T", "east_car_count_T", "west_car_count_T"]
Plus_car_counts = ["north_car_count_Plus", "south_car_count_Plus", "east_car_count_Plus", "west_car_count_Plus"]


def combination(type, dir1, dir2):
    #Starting the required combination
    
    #Accessing the car counts needed
    if type == "T":
        global south_car_count_T, east_car_count_T, west_car_count_T

    elif type == "Plus":
        global north_car_count_Plus, south_car_count_Plus, east_car_count_Plus, west_car_count_Plus 

    display_cars(type)

    print(f"Combination {dir1}-{dir2} for {type}-Intersection: ")
    car_count1 = f"{dir1}_car_count_{type}"
    car_count2 = f"{dir2}_car_count_{type}"

    #Calculating the timer needed
    timer_needed = calculate_timer(2/3*(globals().get(car_count1)) + 2/3*(globals().get(car_count2)), num_lanes=4)
    print(f"Timer taken: {timer_needed}")

    #Calculating the throughput that occured using the found timer
    throughput1 = calculate_throughput(globals().get(car_count1), timer_needed, num_lanes=2)
    throughput2 = calculate_throughput(globals().get(car_count2), timer_needed, num_lanes=2)
    print(f"Number of cars leaving {dir1} road: {throughput1}")
    print(f"Number of cars leaving {dir2} road: {throughput2}")

    #Changing the car counts to their new values
    globals()[car_count1] -= throughput1
    globals()[car_count2] -= throughput2

    display_cars(type)

    #Adding more cars during each combination
    globals()[car_count1] += np.random.randint(10,20)
    globals()[car_count2] += np.random.randint(10,20)
    
    car_list = T_car_counts if type == "T" else Plus_car_counts
    for car_count in car_list:
        if car_count != car_count1 and car_count != car_count2:
            globals()[car_count] += np.random.randint(20, 40)



#Storing the combinations in a list with lambda and calling them when needed
T_combinations = [
    lambda: combination("T", "south", "east"),
    lambda: combination("T", "east", "west"),
    lambda: combination("T", "south", "west")
]

Plus_combinations = [
    lambda: combination("Plus", "north", "south"),
    lambda: combination("Plus", "east", "west"),
    lambda: combination("Plus", "north", "east"),
    lambda: combination("Plus", "south", "west"),
    lambda: combination("Plus", "north", "west"),
    lambda: combination("Plus", "south", "east")
]

#Taking input of the required number of Intersection Combinations
T_main_count = int(input("Enter number of T-combination cycles: "))
Plus_main_count = int(input("Enter number of Plus-combination cycles: "))


#Calling the combinations from the T-Combinations list and Plus_Combinations list
for i in range(T_main_count):
    for func in T_combinations:
        func()

for i in range(Plus_main_count):   
    for func in Plus_combinations:
        func()
