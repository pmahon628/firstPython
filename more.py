# Lists
freinds = ["Jake", "Joel", "Andy", "Kris", 4,]

# refer to elements by index
# can append always to end
freinds.append("Joel")
# insert will add it where you want
freinds.insert(3, "Brendan")
# can remove also
freinds.remove("Jake")
# get the index of item
print(freinds.index("Joel"))
# can get how many like items
print(freinds.count("Andy"))
# sort list - ABC / works for #'s as well
freinds.sort()
# reverse
freinds.reverse()
# create new list as copy
freinds2 = freinds.copy()

# NEW LESSON - TOUPLES
# similar to list - structure to store information
# immutable - cannot be changed, once created, thats it

coordinates = (3, 5)
print(coordinates[3])

# FUNCTIONS
def say_hi(name, age):
    print("Hello " + name + " , you are " +  age)
# calls function that takes in two paramaters
say_hi("Pat", "29")
# Hello Pat, you are 29
# can pass any type of data in

# RETURN STATEMENT
def cube(num):
    return num*num*num
# return key word breaks out of function
result = cube(4)
print(result)

# IF statements
is_male =  True
is_tall  = True 
# check value
# also and condtion - both need to be true in return
if is_male  or  is_tall:
    print("You  are a male or tall or both")
# else if   
elif  is_male and not(is_tall):
    print("You are a short male")

elif not(is_male) and  is_tall:
    print("You are not male  but  are tall")    

else:
    print("You are not a male and not tall")

def max_num(num1, num2, num3):
    if   num_1  >=  num2 and num1 >= num3:
        return  num1
    elif num2 >= num1 and  num2 >=  num3;
       return num2
    else:
        return num3

print(max_num(3, 4, 5))  









