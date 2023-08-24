x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]


#cambia 10 a 15

def valuechange():
    print("cambiando 10 a 15")
    x[1][0]= 15
    print(x)
    z[0]['y']= 30
    print(f'Zeta es {z}')

valuechange()

#Cambia Jordan a Bryant

def last_name_change():
    print("Cambiando nombres")
    estudiantes[0]['last_name']= 'Bryant'
    print(estudiantes)
    directorio_deportes['fútbol'][0] = 'Andrés'
    print(directorio_deportes)

last_name_change()

#Iterar en una lista de diccionarios

def iteratedicts():
    print("Iterando lista de estudiantes")
    
    for dic in estudiantes:
        print(f"{dic['first_name']}-{dic['last_name']} ")
        



iteratedicts()

# solo los valores
def iteratedicts_2(key_name, any_list):
    print("imprimiendo solo valores")
    for dic in any_list:
        
            print(dic[key_name])

iteratedicts_2('first_name', estudiantes)

iteratedicts_2('last_name', estudiantes)


dojo = {
'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def access():
    print(dojo['ubicaciones'][0])

access()

def printinfo(somelist):
    print("mi experimento")
    for key in somelist:
        print (f"{len(somelist[key])} {key.upper()}")
        for each in somelist[key]:
            print(each)
        
    
        
        

printinfo(dojo)