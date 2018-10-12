# Vivek Bannore - BlackBelt Level 1 Assignment

#Only 1 .py file should be created, containing the solution to both the questions below. Use python version 3

# TODO: a) Print the current date and time at the start of the program (hint: use the datetime library and search the internet)

import datetime

dt_format = "%A, %d/%m/%Y %H:%M:%S"
current_dt = datetime.datetime.today()
format_current_dt = current_dt.strftime(dt_format)

print("TODO: (a)")
print("##############################################")

print("The current date & time is - ", format_current_dt)

print("##############################################")
print(" ")
print(" ")


# TODO: b) Print out all the even numbers from the below given list of numbers. Write the solution into a function and have it called in your 
# main block for the requested answer (hint: use loops)

numbers = [{'sequence': '951, 402, 984, 651, 360, 69, 408, 319, 601, 485, 980, 507, 725, 547, 544, 615, 83, 165, 141, 501, 263, 617, 865, 575, 219, 390, 984, 592, 236, 105, 942, 941, 386, 462, 47, 418, 907, 344, 236, 375, 823, 566, 597, 978, 328, 615, 953, 345, 399, 162, 758, 219, 918, 237, 412, 566, 826, 248, 866, 950, 626, 949, 687, 217, 815, 67, 104, 58, 512, 24, 892, 894, 767, 553, 81, 379, 843, 831, 445, 742, 717, 958, 609, 842, 451, 688, 753, 854, 685, 93, 857, 440, 380, 126, 721, 328, 753, 470, 743, 527'}]

print("TODO: (b)")
print("##############################################")

def list_even_num(num):

    for key in numbers:
        # Extract the Values for the Sequence Key
        seq_str = key['sequence']

    # Convert the string list into an interger list 
    seq_list = [int(x) for x in key['sequence'].split(',')]

    print("The even numbers are - ")

    # For Loop to check even numbers & print if even
    for num in range(len(seq_list)):
        if seq_list[num] % 2 == 0:
            print(seq_list[num])

list_even_num(numbers)

print("##############################################")
print(" ")
print(" ")



