#todos los numeros del 0 al 150
print("numeros del 0 a 150")
for var1 in range(0, 151):
    print(var1)


#multiplos de 5
print("Multiplos de 5")
for var2 in range(0,1005, 5):
    print(var2)

#divisible por 5
print ("Contando a la manera dojo")
for var3 in range(0,101):
    if var3 % 10 == 0:
        var3 = "Coding Dojo"
        
    elif var3 % 5 == 0:
        var3 = "Coding"
        
    print(var3)

list1 = list()
for var4 in range (1,5000,2):
    list1.append(var4)
    totalsum =sum(list1)
    
print(totalsum)

#cuenta regresiva
print("cuenta regresiva")
var5= 2018
while var5>0:
    var5 -=4
    print(var5)
else:
    print("termina la cuenta")
    

#contador flexible
print("Contador Flexible")
lownum = 2
highnum=33
mult=3

for var6 in range(lownum, highnum):
    if var6 % mult == 0:
        print(var6)