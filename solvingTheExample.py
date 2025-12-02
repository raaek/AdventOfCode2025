import numpy as np

# translate the original rotaions (e.g. L30) into numbers with plus and minus (e.g. -30)
def translate_rotations_into_numbers(original_rotations):
    print(original_rotations)
    rotations = [-int(elem.replace("L","")) if "L" in elem else int(elem.replace("R","")) for elem in  original_rotations]
    return rotations

# calculate the new dial setting from the old one and the rotation
def calculate_new_dial_setting(current_dial_setting, rotation):
    new_dial_setting = (current_dial_setting + rotation)%100
    print(new_dial_setting)
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

    for rotation in rotations:
        current_dial_setting = calculate_new_dial_setting(current_dial_setting, rotation)
        if current_dial_setting == 0:
            number_of_times_0_has_been_reached+=1

    print("password:\n")
    print(number_of_times_0_has_been_reached)

if __name__=="__main__":
    main()