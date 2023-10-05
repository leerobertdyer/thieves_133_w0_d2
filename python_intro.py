# comments yay

""" 
Doesn't this work too? 
"""

# print("i think it does") 

# I can see that the hashtag actually changes color 
# while the tripple quote does not...
"""correction: it does change color, but it's the same as a standard quote..."""

# ""does this break the code?"" # - sure does

######################### DATA TYPES ##############################
##########          Integers AND Floats          ##################

num1 = 8 #the inline comment
print(num1)
print(type(num1))

num2 = 8.0
print(num2)
print(type(num2))

num3 = 5.123
print(int(num3))

#meth operations (very scary operations)
# print('MAAAAEEEEEETTTTHH!')

add = 1231231 + 123123123123
print(add)

sub = 10 - 9123112.123
print(sub)

mult = .1023 * .023
print(mult)
print(type(mult))

div = 25/.5
print(div)
print(type(div))

pow = 5 ** 5
print(pow)

flooor = 5 // 2
print(flooor) # terrible variable name lol

mod = 5 % 2
print(mod)

# = --> assignment
# == --> comparison (equal)
# != --> comparison (not equal)

print(int('5') == 5)

# 'Protected' words/terms --> careful not to use built in names for variables

#strings

print('\nBILLY FN STRINGS MOFO!\t Yeehaw! \n')

st1 = 'single quot4e string'
st2 = "double quote string"
# st3 = 'we've messed this up'
myString1 = """

    HELLOOOOOOO@! I remembered what triple quotes are for!!!
    '
    "
    "" '''''lklsjdf]\\\qwe]q[weopl;kjf912340192]'''
    
                        I LOVE π
"""

print(myString1.upper())

print(myString1[119])

#manippleation 
#CONCATENATION & INTERPOLATION (f-string)

#concatenation:
print(st1 + ' ' + st2)

f_st = f"This is still a string, but we can say {myString1[-2]}"
print(f_st)

#Incrementing Decrementing

num5 = 234
num6 = 98734
print(num5 + num6)
print(num5, num6)
num5 = num5 + 6
print(num5)
num5 *= num5
print(num5)


#Print is a function
#.upper() is a method for strings
#basically methods are functions used on specific CLASSES (str, int, list, etc...)
# function(arg) ----- datatype.method(arg)

#lists
  #indexed, ordered, iterable, muteable, and dynamic(?)
  #syntax --> alist = [x, y, z]
  
numsList = [10, 20, 30, 40, 50]


print(numsList)

print('\nString example with slicing:')

#lists are mutable I can say numsList[0] = 100, and it changes the list in place
#strings are immutable. I couldn't do that. I could use slicing instead

myStrX = "STRINGS!"
mySlice = "BILLY" + myStrX[:]
print(mySlice)
mySlice = myStrX[::-1]
print(mySlice)


##### FEEELIN LOOOOPY!

test = ['a', 'b', 'c', 'd', 'whoops']
for i in test:
    print(i)
    
#index loop uses in range of...

for i in range(len(test)):
    test[i]+= ' XX'
print(test)


def ageCheck(age):
    if age > 90:
        return('you old yo')
    elif age < 18:
        return('you a kid')
    else:
        return(f'{age} years old aint young or old')

print(ageCheck(1))

age = input('Enter your age: ')
print(ageCheck(int(age)))


user = input('a?')
if 'a' in user:
    print('a in this bitch')
else:
    print('no a here')