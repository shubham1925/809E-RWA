import taskplanning
# print(taskplanning.environment.items())
# requirement_red = taskplanning.red_remaining

# red_in_bin, green_in_bin, blue_in_bin = map(int, input("Enter red, green, blue parts in bins: ").split())
# red_in_kit, green_in_kit, blue_in_kit = map(int, input("Enter red, green, blue parts in kits present already: ").split())
# red_needed, green_needed, blue_needed = map(int, input("Enter red, green, blue parts to place in kit tray: ").split())
#
# red_remaining = red_needed - red_in_kit
# green_remaining = green_needed - green_in_kit
# blue_remaining = blue_needed - blue_in_kit

# taskplanning.red_in_bin, taskplanning.green_in_bin, taskplanning.blue_in_bin = red_in_bin, green_in_bin, blue_in_bin
# print("execpy " + str(taskplanning.red_in_bin))
# taskplanning.red_in_kit, taskplanning.green_in_kit, taskplanning.blue_in_kit = red_in_kit, green_in_kit, blue_in_kit
# taskplanning.red_needed, taskplanning.green_needed, taskplanning.blue_needed = red_needed, green_needed, blue_needed
# taskplanning.red_remaining, taskplanning.green_remaining, taskplanning.blue_remaining = red_remaining, green_remaining, \
#                                                                                         blue_remaining
# Initialize robot at the home position
taskplanning.go_home()

flag_red = False
flag_green = False
flag_blue = False
if taskplanning.red_remaining <= 0:
    print("Red parts already available in the tray, no need to pick up from bins")
    flag_red = True

if taskplanning.green_remaining <= 0:
    print("Green parts already available in the tray, no need to pick up from bins")
    flag_green = True

if taskplanning.blue_remaining <= 0:
    print("Blue parts already available in the tray, no need to pick up from bins")
    flag_blue = True

while not(flag_red):
    taskplanning.move_to_bin()
    taskplanning.pick("red")
    taskplanning.move_to_tray()
    rem_red = taskplanning.place("red")
    # print("Baburao")
    print("rem_red: " + str(rem_red))
# taskplanning.move_to_bin()
# taskplanning.pick("red")
# taskplanning.move_to_tray()
# rem_red = taskplanning.place("red")
# print("rem_red: " + str(rem_red))
    if rem_red == 0:
        print("Exit")
        flag_red = True
    taskplanning.go_home()


print(taskplanning.environment.items())
# We will complete the kit in red, green blue order always
