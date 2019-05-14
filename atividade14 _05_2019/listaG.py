def prod(x):
    if x == 1:
        return 4.00
    elif x == 2:
        return 4.50
    elif x == 3:
        return 5.00
    elif x == 4:
        return 6.00
    elif x == 5:
        return 4.00
    elif x == 6:
        return 6.00
    elif x == 7:
        return 4.50
    elif x == 8:
        return 0.50

def ListaG():
    a = []
    y = 0
    n = int(input('coloque o numero de elementos da lista'))
    while y<2*n:
        b = input('coloque o nome da pessoa na lista')
        a.insert(y,b)
        y+=1
        c = input('coloque o produto da lista')
        a.insert(y,c)
        y+=1
    return a

def ListaGN():
    a = []
    y = 0
    n = int(input('coloque o numero de elementos da lista'))
    h = 0
    while y<3*n:
        b = input('coloque o nome da pessoa na lista')
        a.insert(y,b)
        y+=1
        c = input('coloque o produto da lista')
        a.insert(y,c)
        y+=1
        x = int(input('colque o numero do produto'))
        f = prod(x)
        soma = f+h
        h = f
        a.insert(y,x)
        y+=1
    return(a,soma)
