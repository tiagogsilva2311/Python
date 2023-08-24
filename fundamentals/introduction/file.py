num1 = 42 #Variable numerica
num2 = 2.3 #Variable integral
boolean = True #Variable booleana
string = 'Hello World' #Cadena de caracteres
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #arreglo/lista
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #diccionario
fruit = ('blueberry', 'strawberry', 'banana') #Tupla
print(type(fruit)) #Type check
print(pizza_toppings[1]) #access value
pizza_toppings.append('Mushrooms') #add value
print(person['name']) #dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary add value
print(fruit[2]) #tuple add value

if num1 > 45: #conditional
    print("It's greater")
else: #else
    print("It's lower")

if len(string) < 5: #conditional length check
    print("It's a short word!")
elif len(string) > 15: #elseif length check
    print("It's a long word!")
else:
    print("Just right!") #else

for x in range(5): #for s start
    print(x)
for x in range(2,5): #for (start,stop)
    print(x)
for x in range(2,10,3): #for (start, stop, increment)
    print(x)
x = 0 #variable declaration
while(x < 5): #While loop start
    print(x)
    x += 1 #while increment

pizza_toppings.pop() #List delete value
pizza_toppings.pop(1) #list delete value in index 1

print(person) #dictionary access values
person.pop('eye_color') #dictionary delete value
print(person)

for topping in pizza_toppings: #for loop
    if topping == 'Pepperoni': #conditional
        continue #increment
    print('After 1st if statement')
    if topping == 'Olives':
        break #break

def print_hello_ten_times(): #function
    for num in range(10): #parameter
        print('Hello')

print_hello_ten_times()

def print_hello_x_times(x): #function x=argument
    for num in range(x):
        print('Hello')

print_hello_x_times(4) #function argument is 4

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3) NameError: name <num3> is not defined
# num3 = 72 -->var declaration
# fruit[0] = 'cranberry'--> change value
# print(person['favorite_team'])-->KeyError: 'favorite_team'
# print(pizza_toppings[7])-- IndexError: list index out of range
#   print(boolean) IndentationError: unexpected indent
# fruit.append('raspberry') - AttributeError: 'tuple' object has no attribute 'append'
# fruit.pop(1) - AttributeError: 'tuple' object has no attribute 'pop'