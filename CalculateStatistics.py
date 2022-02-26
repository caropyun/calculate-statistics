from TempDataSet import TempDataSet

docstring = """ CalculateStatistics
    Submitted by Carolyn Pyun  
    Submitted:  3/23/21
    - This program simulates a menu screen/ dashboard by printing 
    lines of text to the screen depending on which choice on the menu 
    the user inputs. Doesn't quit until 7 is entered.
    - Able to load data and name the data with menu option 1
    - Can change the temperature units in menu option 2
    - Prints and sorts list of sensors by room number, and list of active sensors.
    User is able to toggle sensors active or deactivate them with menu option 3.
    - Shows stats regarding active sensors in menu option 4
    - TempDataSet: Manages temperature data, data encapsulated into this class.
"""


def recursive_sort(list_to_sort, key=0, length=-1):
    """Given a list and key for dictionaries, sorts recursively with BubbleSort in order"""
    sensor_to_swap = list_to_sort.copy()
    # find the original length
    if length == -1:
        length = len(sensor_to_swap)

    # exit
    if length == 1:
        return sensor_to_swap

    # swap bubble sort
    for i in range(length - 1):
        if sensor_to_swap[i][key] > sensor_to_swap[i + 1][key]:
            sensor_to_swap[i], sensor_to_swap[i + 1] = sensor_to_swap[i + 1], sensor_to_swap[i]

    return recursive_sort(sensor_to_swap, key, length - 1)


def test_sensor_setup(sensor_list, active_sensors):
    """Tests the sensor setups. Sensors vs active sensors."""
    print("\nTesting sensor_list length:")
    if len(sensor_list) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing sensor_list content:")
    rooms_list = [i[0] for i in sensor_list]
    descriptions_list = [i[1] for i in sensor_list]
    if "4213" not in rooms_list or "Out" not in rooms_list:
        print("Fail - something is wrong with the room numbers")
    elif "Foundations Lab" not in descriptions_list:
        print("Fail - something is wrong with room descriptions")
    else:
        print("Pass")

    print("Testing active_sensors length:")
    if len(active_sensors) == 6:
        print("Pass")
    else:
        print("Fail")

    print("Testing active_sensors content:")
    if sum(active_sensors) == 20:
        print("Pass")
    else:
        print("Fail")


def print_header():
    print("\nSTEM Center Temperature Project")
    print("Carolyn Pyun")


# passes float celsius value and int units returns conversion to either C,F,K
def convert_units(celsius_value, units):
    # if 0, temperature in celsius
    if units == 0:
        return celsius_value;

    # if 1, return fahrenheit
    elif units == 1:
        return celsius_value * 1.8 + 32

    # if 2, return kelvin
    else:
        return celsius_value + 273.15


def print_menu():
    """ Prints the main menu onto screen for user to choose:
        Main Menu
        ---------
        1 - Process a new data file
        2 - Choose units
        3 - Edit room filter
        4 - Show summary statistics
        5 - Show temperature by date and time
        6 - Show histogram of temperatures
        7 - Quit
    """
    print("\nMain Menu\n---------")
    print("1 - Process a new data file")
    print("2 - Choose units")
    print("3 - Edit room filter")
    print("4 - Show summary statistics")
    print("5 - Show temperature by date and time")
    print("6 - Show histogram of temperatures")
    print("7 - Quit")


# when user chooses 1
def new_file(dataset):
    """ Open a new file
    """
    print("Called new_file() function.")


current_unit = 0
UNITS = {
    0: ("Celsius", "C"),
    1: ("Fahrenheit", "F"),
    2: ("Kelvin", "K"),
}


# when user chooses 2
def choose_units():
    """User chooses units from the list of avaliabel units"""
    global current_unit

    global UNITS

    # reports current units
    units_list = UNITS[current_unit]
    print(f"Current units in {units_list[0]}")
    unit_valid = False
    while unit_valid == False:
        # give menu of available units
        print("Choose new units:")
        for key in UNITS:
            print(f"{key} - {UNITS[key][0]}")

        # ask user to choose new unit
        print("Which unit? [Enter 0, 1 or 2]")

        # checks if the user input is a number
        try:
            new_unit = int(input())
        except ValueError:
            print("Error: Invalid input. Enter a number only.")
            unit_valid = False
            continue

        # check if user input is valid
        if new_unit in UNITS:
            unit_valid = True
            current_unit = new_unit
        else:
            print("Please choose a unit from the list.")
            unit_valid = False


# when user chooses 3
def print_filter(sensor_list, active_sensors):
    """Prints list of sensors, noting which ones are active"""
    print("Printing filtered sensor list.")
    for sensors in sensor_list:
        # prints Room Number: Room Name [ACTIVE] (or not)
        if sensors[2] in active_sensors:
            print(f"{sensors[0]}: {sensors[1]} [ACTIVE]")
        else:
            print(f"{sensors[0]}: {sensors[1]}")


def change_filter(sensor_list, active_sensors):
    """Toggles sensors on and off as user enters room numbers
        calls print_filter to print filtered list"""
    print("Called change_filter() function.")
    # dictionary, room num as key, sensor num as value
    sensors = {}
    for sens in sensor_list:
        sensors[sens[0]] = sens[2]
    print("sensor_dict =", sensors)

    filter_list = []
    user_input = ""
    # until user enters x to exit
    while user_input != "x":
        # print the state of sensors (active or not)
        print_filter(sensor_list, active_sensors)
        print()
        user_input = input("Type the sensor number to toggle (e.g. 4201) or x to end: ")
        if user_input == "x":
            break
        # if valid room
        try:
            sensor = sensors[user_input]
            print(f"Room {user_input} found {sensor} in list.")
            # if active, deactivate and vice versa
            if sensor in active_sensors:
                active_sensors.remove(sensor)
            else:
                active_sensors.append(sensor)
            # add to list of which ones are deactivated
            if sensor in filter_list:
                filter_list.remove(sensor)
            else:
                filter_list.append(sensor)
            print("filter list =", filter_list)
        # not a valid room
        except KeyError:
            print(f"Invalid sensor {user_input}. Please try again.")


#       If there is no data, display a warning message and return.
#       Otherwise prints out the current data set name, and the minimum,
#       maximum and average temperature in the current unit.
def print_summary_statistics(dataset, active_sensors):
    """"Display a summary of the data collected.
    """
    if dataset is None or len(active_sensors) == 0 or active_sensors is None or dataset.get_summary_statistics(
            active_sensors) is None:
        print("Please load data file and make sure at least one sensor is active.")
    else:
        print(f"Summary statistics for {dataset.get_name}")
        stats = dataset.get_summary_statistics(active_sensors)
        stats = (round(stats[0], 2), round(stats[1], 2), round(stats[2], 2))
        print(f"Minimum Temperature: {convert_units(stats[0], current_unit)} {UNITS[current_unit][1]}")
        print(f"Maximum Temperature: {convert_units(stats[1], current_unit)} {UNITS[current_unit][1]}")
        print(f"Average Temperature: {convert_units(stats[2], current_unit)} {UNITS[current_unit][1]}")


def print_temp_by_day_time(dataset, active_sensors):
    """ Print temperature by day time
    """
    print("Called print_temp_by_day_time() function.")


def print_histogram(dataset, active_sensors):
    """ Print histogram
    """
    print("Called print_histogram() function.")


def new_file(dataset, file_path=""):
    file_path = input("Please enter the path and file name of the new dataset: ")
    try:
        dataset.process_file(file_path)
        print(f"Loaded {dataset.get_loaded_temps()} samples.")
    except FileNotFoundError:
        print("File not found.  Unable to load file.")
        return

    name_for_data = input("Enter a 3-20 character name for the data: ")
    while len(name_for_data) < 3 or len(name_for_data) > 20:
        name_for_data = input("Bad name, try again.")
        try:
            dataset.set_name(name_for_data)
        except TypeError:
            continue
    dataset.set_name(name_for_data)


def main():
    the_sensor_list = [("4213", "STEM Center", 0), ("4201", "Foundations Lab", 1),
                       ("4204", "CS Lab", 2), ("4218", "Workshop Room", 3),
                       ("4205", "Tiled Room", 4), ("Out", "Outside", 10)]
    the_active_sensors = [the_sensor_list[i][2] for i in range(6)]

    # Provides a sorted list of sensors by room number.
    sorted_by_room = recursive_sort(the_sensor_list)
    # print(f"sensors by room number {sorted_by_room}")
    # print(f"active_list is {the_active_sensors}")

    # Create an object of type TempDataSet
    current_set = TempDataSet()
    print_header()
    print_menu()
    print(f"The average temperature is {current_set.get_avg_temperature_day_time(the_active_sensors, 5, 7)}")
    # - choose function call based on menu selection
    user_selection = 0

    # Keeps asking user for a menu selection and runs it if valid selection
    # until the user selects 7 to quit.
    while user_selection != 7:
        # debug_data_set = current_set.data_set
        # if debug_data_set is not None:
        #    print([debug_data_set[k] for k in range(0, 5000, 1000)])

        print("Enter [1-7] for the menu option you would like to select: ")
        # checks if the user input is a number
        try:
            user_selection = int(input())
        except ValueError:
            print("Error: Invalid input. Enter a number only.")
            continue

        if user_selection == 7:
            break
        # checks if number input isn't a choice on menu
        if user_selection > 7 or user_selection < 1:
            print("Invalid selection.")
        # valid selection so run methods
        if user_selection == 1:
            new_file(current_set)
            # current_set.process_file("resources/Temperatures_0806.csv")
            # current_set.process_file("DoesNotExist")
        elif user_selection == 2:
            choose_units()
        elif user_selection == 3:
            change_filter(sorted_by_room, the_active_sensors)
        elif user_selection == 4:
            print_summary_statistics(current_set, the_active_sensors)
        elif user_selection == 5:
            print_temp_by_day_time(None, None)
        elif user_selection == 6:
            print_histogram(None, None)
        print_menu()
        print(f"The average temperature is {current_set.get_avg_temperature_day_time(the_active_sensors, 5, 7)}")

    # Displays concluding thank you message.
    print("Thank you for using the STEM Center Temperature Project")


if __name__ == '__main__':
    main()
