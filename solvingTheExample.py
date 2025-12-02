import numpy as np
import math

# translate the original rotaions (e.g. L30) into numbers with plus and minus (e.g. -30)
def translate_rotations_into_numbers(original_rotations):
    # print(original_rotations)
    rotations = [-int(elem.replace("L","")) if "L" in elem else int(elem.replace("R","")) for elem in  original_rotations]
    return rotations

# calculate the new dial setting from the old one and the rotation
def calculate_new_dial_setting(current_dial_setting, rotation):
    new_dial_setting = (current_dial_setting + rotation)%100
    # print(new_dial_setting)
    return new_dial_setting

def main():

    number_of_times_0_has_been_reached = 0 # will be the password
    initial_dial_setting = 50
    current_dial_setting = initial_dial_setting

    # name of the input file with the rotation instructions
    input_file = "input.txt"
    original_rotations = []
    # read in the settings from the file
    with open (input_file) as file:
        for line in file.readlines():
            original_rotations.append(line.rstrip())

    rotations = translate_rotations_into_numbers(original_rotations)

    print("the dial starts by pointing at ", current_dial_setting)
    for rotation in rotations:
        sum = current_dial_setting + rotation
        print("the dial is rotated ", rotation, "to point at ", sum%100)
        if sum>=100:
            number_of_times_0_has_been_reached = number_of_times_0_has_been_reached + math.floor(sum/100)
            print("during this rotation, it points at 0 ", math.floor(sum/100), " times")
        if sum<=0:
            number_of_times_0_has_been_reached = number_of_times_0_has_been_reached + 1 + math.floor(np.abs(sum)/100)
            print("during this rotation, it points at 0 ", 1 + math.floor(np.abs(sum)/100), " times")
            if current_dial_setting == 0:
                number_of_times_0_has_been_reached = number_of_times_0_has_been_reached - 1

        current_dial_setting = calculate_new_dial_setting(current_dial_setting, rotation)

    print("password:\n", number_of_times_0_has_been_reached)

if __name__=="__main__":
    main()