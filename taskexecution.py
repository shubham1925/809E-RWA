import taskplanning

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

# We will complete the kit in red, green blue order always

while not(flag_red):
    taskplanning.move_to_bin()
    taskplanning.pick("red")
    taskplanning.move_to_tray()
    rem_red = taskplanning.place("red")
    # print("Baburao")
    print("rem_red: " + str(rem_red))
    if rem_red == 0:
        print("Exit")
        flag_red = True
    taskplanning.go_home()

while not(flag_green):
    taskplanning.move_to_bin()
    taskplanning.pick("green")
    taskplanning.move_to_tray()
    rem_green = taskplanning.place("green")
    if rem_green == 0:
        print("Exit")
        flag_green = True
    taskplanning.go_home()

while not(flag_blue):
    taskplanning.move_to_bin()
    taskplanning.pick("blue")
    taskplanning.move_to_tray()
    rem_green = taskplanning.place("blue")
    if rem_green == 0:
        print("Exit")
        flag_blue = True
    taskplanning.go_home()

if flag_red and flag_green and flag_blue:
    taskplanning.environment["KitStatus"]["kit_complete"] = True

print(taskplanning.environment.items())
