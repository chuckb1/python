num1 = 42 # numbers, variable declaration
num2 = 2.3 # numbers, variable declaration
boolean = True #boolean
string = 'Hello World' # - variable declaration, strings
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, strings
print(type(fruit))
print(pizza_toppings[1])
pizza_toppings.append('Mushrooms')
print(person['name'])
person['name'] = 'George'
person['eye_color'] = 'blue'
print(fruit[2])
# conditional
if num1 > 45: #if
    print("It's greater")
else: #else
    print("It's lower")

if len(string) < 5: #if
    print("It's a short word!")
elif len(string) > 15: #else if
    print("It's a long word!")
else:
    print("Just right!")
#for loop
for x in range(5): 
    print(x)
for x in range(2,5): # for loop
    print(x)
for x in range(2,10,3): # for loop
    print(x)
x = 0 #start, variable declaration
while(x < 5): # while loop, stop
    print(x) 
    x += 1  # increment

pizza_toppings.pop() #
pizza_toppings.pop(1) #

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings: #for loop, start, increment
    if topping == 'Pepperoni': # conditional, if
        continue # continue
    print('After 1st if statement') #return
    if topping == 'Olives': #conditional, if
        break # break

def print_hello_ten_times(): # function
    for num in range(10):   # parameter
        print('Hello')      # return

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

# comment
# multiline
"""
Bonus section
"""
# single line, dictionary
# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)