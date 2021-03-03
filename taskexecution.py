import taskplanning
from termcolor import colored

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
    print(colored('Starting with red parts..', 'red'))
    taskplanning.move_to_bin()
    taskplanning.pick("red")
    taskplanning.move_to_tray()
    rem_red = taskplanning.place("red")
    # print("Baburao")
    # print("rem_red: " + str(rem_red))
    print("\n")
    if rem_red == 0:
        print("Exit")
        flag_red = True
    taskplanning.go_home()

while not(flag_green):
    print(colored('Starting with green parts..', 'green'))
    taskplanning.move_to_bin()
    taskplanning.pick("green")
    taskplanning.move_to_tray()
    rem_green = taskplanning.place("green")
    if rem_green == 0:
        print("Exit")
        flag_green = True
    taskplanning.go_home()

while not(flag_blue):
    print(colored('Starting with blue parts..', 'blue'))
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

print("\n")

print(f'Parts remaining in red bin: {taskplanning.environment["PartsInBins"]["red_parts"]}')
print(f'Parts remaining in green bin: {taskplanning.environment["PartsInBins"]["green_parts"]}')
print(f'Parts remaining in blue bin: {taskplanning.environment["PartsInBins"]["blue_parts"]}\n')

print(f'Parts in red kit: {taskplanning.environment["PartsInKit"]["red_in_kit"]}')
print(f'Parts in green kit: {taskplanning.environment["PartsInKit"]["green_in_kit"]}')
print(f'Parts in blue kit: {taskplanning.environment["PartsInKit"]["blue_in_kit"]}\n')

print(taskplanning.environment.items())
