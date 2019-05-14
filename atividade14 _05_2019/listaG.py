#este arquivo contem as funções dos progamas 
def prod(x):
    if x == 1:# numero do produto
        return 4.00#valor do produto
    elif x == 2:# numero do produto
        return 4.50#valor do produto
    elif x == 3:# numero do produto
        return 5.00#valor do produto
    elif x == 4:# numero do produto
        return 6.00#valor do produto
    elif x == 5:# numero do produto
        return 4.00#valor do produto
    elif x == 6:# numero do produto
        return 6.00#valor do produto
    elif x == 7:# numero do produto
        return 4.50#valor do produto
    elif x == 8:# numero do produto
        return 0.50#valor do produto

def ListaG():
    a = []#lista vazia
    y = 0#contador para colocar o local do elemento na lista
    n = int(input('coloque o numero de elementos da lista'))#numero de elementos na lista
    while y<2*n: #repetição
        b = input('coloque o nome da pessoa na lista')#nomes
        a.insert(y,b)#local na lista e o elemento
        y+=1#adiciona 1 ao contador
        c = input('coloque o produto da lista')#produto
        a.insert(y,c)#local na lista e o elemento
        y+=1#adiciona 1 ao contador
    return a#retorna a lista

def ListaGN():
    a = []#lista vazia
    y = 0#contador para colocar o local do elemento na lista
    n = int(input('coloque o numero de elementos da lista'))
    h = 0#será utilizado para fazer a soma portanto o valor inicial deve ser zero
    while y<3*n:
        b = input('coloque o nome da pessoa na lista')
        a.insert(y,b)#local na lista e o elemento
        y+=1#adiciona 1 ao contador#adiciona 1 ao contador
        c = input('coloque o produto da lista')
        a.insert(y,c)#local na lista e o elemento
        y+=1#adiciona 1 ao contador
        x = int(input('colque o numero do produto'))
        f = prod(x)#função prod
        soma = f+h#soma para obter a soma 
        h = f# armazena o valor de f
        a.insert(y,x)#local na lista e o elemento
        y+=1#adiciona 1 ao contador
    return(a,soma)#retorna a lista e a soma
