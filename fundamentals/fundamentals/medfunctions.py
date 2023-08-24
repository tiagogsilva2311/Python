#Primera parta

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

#cambiar un valor de x
def changevalue():
    print ("cambiando el valor de 10 a 15")
    x[1][0] = 15 
    print(x)

changevalue()


#Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
def changestudentname():
    print("cambio de nombre")
    estudiantes[0]['last_name'] = 'Bryant'  
    print(estudiantes)

changestudentname()