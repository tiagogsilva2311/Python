#Basic Functions
#hace runa cuenta regresiva
def countdown(time):
    while time> 0:
        time -= 1
        print(time)
    else:
        print ("No time left")

countdown(2000)

#poner lista en función, imprimit 1er valor retornar segundo

def lfuncion(ulist = []):

    print(ulist[0])
    return ulist [1]
    

lfuncion([2,4])


