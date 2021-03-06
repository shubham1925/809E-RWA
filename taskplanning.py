red_in_bin, green_in_bin, blue_in_bin = map(int, input("Enter red, green, blue parts in bins: ").split())
if red_in_bin < 0 or green_in_bin < 0 or blue_in_bin < 0:
    print("Enter positive values for parts present in bin\n")
    red_in_bin, green_in_bin, blue_in_bin = map(int, input("Enter red, green, blue parts in bins: ").split())

red_in_kit, green_in_kit, blue_in_kit = map(int, input("Enter red, green, blue parts in kits present already: ").split())
if red_in_kit < 0 or green_in_kit < 0 or blue_in_kit < 0:
    print("Enter positive values for parts present in the kit\n")
    red_in_kit, green_in_kit, blue_in_kit = map(int,
                                                input("Enter red, green, blue parts in kits present already: ").split())

red_needed, green_needed, blue_needed = map(int, input("Enter red, green, blue parts to place in kit tray: ").split())
if red_needed < 0 or blue_needed < 0 or green_needed < 0:
    print("Enter positive values for parts required in the kit\n")
    red_needed, green_needed, blue_needed = map(int,
                                                input("Enter red, green, blue parts to place in kit tray: ").split())

print("\n")

red_remaining = red_needed - red_in_kit
green_remaining = green_needed - green_in_kit
blue_remaining = blue_needed - blue_in_kit

yet_to_go_red, yet_to_go_green, yet_to_go_blue = 0, 0, 0

if red_remaining > red_in_bin or green_remaining > green_in_bin or blue_remaining > blue_in_bin:
    print("Demand exceeds availability. Exiting..")
    exit()

if red_remaining >= 0:
    print(f"Red parts required: {red_remaining}")
if green_remaining >= 0:
    print(f"Green parts required: {green_remaining}")
if blue_remaining >= 0:
    print(f"Blue parts required: {blue_remaining}")
print("\n")

environment = {
    "RobotLocation": {
        # True indicates the presence of robot at that position
        "at_home": True,
        "at_bin":  False,
        "at_tray":  False
    },
    "GripperStatus": {
        # False indicates that the gripper is empty
        "gripper_left": False,
        "gripper_right": False
    },
    "KitStatus": {
        # False indicates that the kit is incomplete
        "kit_complete": False
    },
    "PartsInBins": {
        "red_parts": red_in_bin,
        "green_parts": green_in_bin,
        "blue_parts": blue_in_bin
    },
    "PartsInKit": {
        "red_in_kit": red_in_kit,
        "green_in_kit": green_in_kit,
        "blue_in_kit": blue_in_kit
    }
}


def go_home():
    """ Function to set the robot parameters to home condition"""
    # Set grippers to empty/false
    environment["GripperStatus"]["gripper_left"] = False
    environment["GripperStatus"]["gripper_right"] = False

    # Set robot at home position
    environment["RobotLocation"]["at_home"] = True
    environment["RobotLocation"]["at_bin"] = False
    environment["RobotLocation"]["at_tray"] = False

    print("Robot is now at home")


def move_to_bin():
    """ Function to move the robot to the bin, by changing the RobotLocation parameters in the dictionary """
    # Pre-requisite
    robot_location = environment.get("RobotLocation").get("at_bin")
    gripper_condition_left = environment.get("GripperStatus").get("gripper_left")
    gripper_condition_right = environment.get("GripperStatus").get("gripper_right")
    kit_complete = environment.get("KitStatus").get("kit_complete")

    # Effect
    if gripper_condition_right is False and gripper_condition_left is False and kit_complete is False and \
            robot_location is False:
        environment["RobotLocation"]["at_bin"] = True
        environment["RobotLocation"]["at_home"] = False
        environment["RobotLocation"]["at_tray"] = False
        print("Robot moved to bin")


def move_to_tray():
    """ Function to move the robot to the tray, by changing the RobotLocation parameters in the dictionary """
    # Pre-requisite
    robot_location = environment.get("RobotLocation").get("at_tray")
    gripper_condition_left = environment.get("GripperStatus").get("gripper_left")
    gripper_condition_right = environment.get("GripperStatus").get("gripper_right")
    kit_complete = environment.get("KitStatus").get("kit_complete")

    # Effect
    if (gripper_condition_right is True or gripper_condition_left is True) and kit_complete is False and \
            robot_location is False:
        environment["RobotLocation"]["at_bin"] = False
        environment["RobotLocation"]["at_home"] = False
        environment["RobotLocation"]["at_tray"] = True
        print("Robot moved to tray")


def pick(part_color):
    """ Function to pick the part of color specified by the variable part_color from the bin"""
    print("Robot moving to pick part")
    global red_remaining
    global green_remaining
    global blue_remaining
    # Pre-requisites
    gripper_condition_left = environment.get("GripperStatus").get("gripper_left")
    gripper_condition_right = environment.get("GripperStatus").get("gripper_right")
    robot_location = environment.get("RobotLocation").get("at_bin")
    if robot_location is False:
        # environment["RobotLocation"]["at_home"] = False
        # print("Robot not at home position\n")
        environment["RobotLocation"]["at_bin"] = True
        print("Robot moved to bin")

    if part_color == "red":
        part_to_pick = environment.get("PartsInBins").get("red_parts")
        parts_remaining = red_remaining
    elif part_color == "green":
        part_to_pick = environment.get("PartsInBins").get("green_parts")
        parts_remaining = green_remaining
    else:
        part_to_pick = environment.get("PartsInBins").get("blue_parts")
        parts_remaining = blue_remaining
    kit_complete_condition = environment.get("KitStatus").get("kit_complete")

    # Effects
    if parts_remaining >= 2:
        gripper_condition_left = True
        environment["GripperStatus"]["gripper_left"] = True
        gripper_condition_right = True
        environment["GripperStatus"]["gripper_right"] = True
        if part_color == "red":
            # Update parts in bins
            environment["PartsInBins"]["red_parts"] = part_to_pick - 2
            red_remaining = red_remaining - 2
        elif part_color == "green":
            environment["PartsInBins"]["green_parts"] = part_to_pick - 2
            green_remaining = green_remaining - 2
        else:
            environment["PartsInBins"]["blue_parts"] = part_to_pick - 2
            blue_remaining = blue_remaining - 2
        print(f"Robot picked 2 {part_color} parts with both hands")
        # print(f"Parts of {part_color} remaining to be picked: " + str(part_to_pick - 2))
    else:
        # If there is a single part to be picked up, we assume that it will picked up with the left gripper always
        gripper_condition_left = True
        environment["GripperStatus"]["gripper_left"] = True
        gripper_condition_right = False
        environment["GripperStatus"]["gripper_right"] = False
        if part_color == "red":
            environment["PartsInBins"]["red_parts"] = part_to_pick - 1
            red_remaining = red_remaining - 1
        elif part_color == "green":
            environment["PartsInBins"]["green_parts"] = part_to_pick - 1
            green_remaining = green_remaining - 1
        else:
            environment["PartsInBins"]["blue_parts"] = part_to_pick - 1
            blue_remaining = blue_remaining - 1
        print(f"Robot picked one {part_color} part with left hand")


def place(part_color):
    """ Function to place the part in the kit, color is specified by variable part_color"""
    gripper_condition_left = environment.get("GripperStatus").get("gripper_left")
    gripper_condition_right = environment.get("GripperStatus").get("gripper_right")
    robot_location = environment.get("RobotLocation").get("at_tray")
    kit_complete_condition = environment.get("KitStatus").get("kit_complete")
    if part_color == "red":
        parts_already_present = environment.get("PartsInKit").get("red_in_kit")
    elif part_color == "green":
        parts_already_present = environment.get("PartsInKit").get("green_in_kit")
    else:
        parts_already_present = environment.get("PartsInKit").get("blue_in_kit")

    if gripper_condition_right == True and gripper_condition_left == True:
        # Both hands are grasping some part
        print(f"Robot placed the {part_color} parts in kit")
        if part_color == "red":
            environment["PartsInKit"]["red_in_kit"] = parts_already_present + 2
            print(f"Parts of {part_color} remaining to be picked are: " + str(red_needed - parts_already_present - 2))
            global yet_to_go_red
            yet_to_go_red = red_needed - parts_already_present - 2
            environment["GripperStatus"]["gripper_left"] = False
            environment["GripperStatus"]["gripper_left"] = False
        elif part_color == "green":
            environment["PartsInKit"]["green_in_kit"] = parts_already_present + 2
            print(f"Parts of {part_color} remaining to be picked are: " + str(green_needed - parts_already_present - 2))
            global yet_to_go_green
            yet_to_go_green = green_needed - parts_already_present - 2
            environment["GripperStatus"]["gripper_left"] = False
            environment["GripperStatus"]["gripper_left"] = False
        else:
            environment["PartsInKit"]["blue_in_kit"] = parts_already_present + 2
            print(f"Parts of {part_color} remaining to be picked are: " + str(blue_needed - parts_already_present - 2))
            global yet_to_go_blue
            yet_to_go_blue = blue_needed - parts_already_present - 2
            environment["GripperStatus"]["gripper_left"] = False
            environment["GripperStatus"]["gripper_left"] = False
    elif gripper_condition_left == True and gripper_condition_right == False:
        print(f"Robot placed the {part_color} part in the kit")
        if part_color == "red":
            environment["PartsInKit"]["red_in_kit"] = parts_already_present + 1
            print(f"Parts of {part_color} remaining to be picked are: " + str(str(red_needed - parts_already_present - 1)))
            yet_to_go_red = red_needed - parts_already_present - 1
            environment["GripperStatus"]["gripper_left"] = False
        elif part_color == "green":
            environment["PartsInKit"]["green_in_kit"] = parts_already_present + 1
            print(f"Parts of {part_color} remaining to be picked are: " + str(str(green_needed - parts_already_present - 1)))
            yet_to_go_green = green_needed - parts_already_present - 1
            environment["GripperStatus"]["gripper_left"] = False
        else:
            environment["PartsInKit"]["blue_in_kit"] = parts_already_present + 1
            print(f"Parts of {part_color} remaining to be picked are: " + str(str(blue_needed - parts_already_present - 1)))
            yet_to_go_blue = blue_needed - parts_already_present - 1
            environment["GripperStatus"]["gripper_left"] = False
    environment["RobotLocation"]["at_tray"] = True
    if part_color == "red":
        return yet_to_go_red
    elif part_color == "green":
        return yet_to_go_green
    else:
        return yet_to_go_blue
