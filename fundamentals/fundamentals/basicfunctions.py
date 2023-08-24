#cuenta regresiva
def countdown(time):
    
    while time >=0:
        print(time)
        time -=1
    else:
        print("se acabó el conteo")


#lista en función
print("cuenta regresiva")
countdown(5000)

def listreturn(lista=[1,2]):
    
    print (lista[0])
    return lista[1]
    
    
    
    

print("lista en función")
listreturn([2,3])
listreturn ([80,40])

#sum the first index of the list plus the length of the list
def listsum(inputlist=[]):
    total = inputlist[0] + len(inputlist) 
    print(total)

print("Sum the first index plus the length")
listsum([1,2,3])
listsum([1,3,5,8,10])

# Lista de valores mayores que el segundo índice
def morethansecondindex(firstlist=[]):
    list2=[]
    for each in firstlist:
        if each>firstlist[1]:
            list2.append(each)
            
    print(list2)

print("Lista de  numeros  mayor al segundo indice")
morethansecondindex([1,5,5,8,4,6])

#must stabilish lenght and value, function must create a list that prints the value a number of times equal to length
def lengthandvalue(length,value):
    list1=[]
    
    while length>0:
        list1.append(value)
        length -=1
    print(list1)




print("imprime una lista del segundo numero un numero de veces igual al primero")
lengthandvalue(8,1)
