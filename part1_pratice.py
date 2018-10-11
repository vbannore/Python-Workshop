# TODO: 1. Write a Python function that takes a sequence of numbers and determines if all the numbers 
# are different from each other.

# generate a sequence of numbers from 1 to 10
seq_num = [x for x in range(10)]
#seq_num = [0,1,2,3,4,0,5,4,3,10]
#print(seq_num)
#print(type(seq_num))
#print(len(seq_num))

def compare_seq_nums(list_num):
    import itertools
    import math

    # length of sequence
    n = len(list_num)
    # amount of numbers to compare in each combination
    r = 2
    # total number of combinations, nCr = n! / r! (n - r)!
    num_comb = math.factorial(n) / (math.factorial(r)*math.factorial(n - r))

    # a basic counter
    counter = 0

    for a, b in itertools.combinations(list_num, r):
        #print(a,b)        
        if a == b:
            counter += 1  
    

    if counter > 0:
        print(list_num)
        print("There are some numbers repeated in the list")
    else:
        print(list_num)
        print("All numbers are different from each other")

print("TODO: 1")
print("##############################################")
compare_seq_nums(seq_num)        
print("##############################################")
print(" ")
print(" ")

# TODO: 2. Write a Python program that accept a positive number and subtract from this number the sum 
# of its digits and so on. Continues this operation until the number is positive.

# Not ver clear if the difference that results from the first input - sum of those digits should again be going through this iteration 

print("TODO: 2")
print("##############################################")

input_num=int(input("Enter atleast a 2 or more-digit positive number:"))
dup_input_num = input_num
sum_digits=0
diff = input_num
last_positive_num = 0

def add_digits(num):
    sum_digits = 0
    while(num > 0):
        digit = num % 10
        sum_digits = sum_digits + digit
        num = num // 10
    return sum_digits    


def sub_digits(num):
    diff = 0
    diff = num - add_digits(num) 
    return diff
    
#sum_digits = add_digits(input_num)
#print(sum_digits)
subt = sub_digits(input_num)
print(subt)

while subt > 0:
    subt = sub_digits(subt)
    #print(subt)
    if subt > 0:
        last_positive_num = subt 

    
#print("The total sum of digits is:",sum_digits) 
print("The last positive number :",last_positive_num) 
print("##############################################")
print(" ")
print(" ")


# TODO: 3. Write a Python program to find the digits which are absent in a given mobile number

print("TODO: 3")
print("##############################################")

# mobile number
mob_num_digits = [1,3,2,4,5,6,0,7,8,9]
#print(mob_num_digits)

# list to compare the mobile number against
compare_list = [0,1,2,3,4,5,6,7,8,9]

# convert to set
compare_list = set(compare_list)

# convert mobile number to set
mob_num = set(mob_num_digits)

# compare
missing_num = list(mob_num ^ compare_list)

if len(missing_num) == 0:
    print("There are no numbers missing")
else:
    print("The following numbers are missing from the mobile number: ", missing_num)


print("##############################################")
print(" ")
print(" ")


# TODO: 4. Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. 
# Use the characters exactly once.

print("TODO: 4")
print("##############################################")
import itertools  
original_str = "aeiou"

print("The strings are: ")

for a in itertools.permutations(original_str):
    print("".join(a))

print(" ")
print("##############################################")
print(" ")
print(" ")


# TODO: 5. Write a Python program to find common divisors between two numbers in a given pair.

print("TODO: 5")
print("##############################################")
num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))

cd_num = 0

cd = []

for a in range(1, min(num1, num2)+1): 
    if (num1 % a) == (num2 % a) == 0: 
        cd.append(a)
        cd_num += 1
      
print("Number of common divisors: ",cd_num) 
print("The common divisors: ",cd) 
print("##############################################")
print(" ")
print(" ")

