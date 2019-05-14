import listaG as L

print('1 - Salgado, 2 - Refrigerante, 3- Suco, 4 - Sorvete, 5 - Cafe , 6 - Capuccino , 7 - Bolo, 8 - Dadinho')
a = int(input('coloque o numero do produto'))
L.prod(a)
print('valor do produto:',L.prod(a))
