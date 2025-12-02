import numpy as np

# read in the settings from the file and translate into a number

def calculate_new_dial_setting(current_dial_setting, rotation):
    new_dial_setting = (current_dial_setting + rotation)%99
    print(new_dial_setting)
    return new_dial_setting

counter = 0
initial_dial_setting = 50
current_dial_setting = initial_dial_setting

for rotation in rotations:
    current_dial_setting = calculate_new_dial_setting(current_dial_setting, rotation)
    if current_dial_setting == 0:
        counter+=1

print(counter)