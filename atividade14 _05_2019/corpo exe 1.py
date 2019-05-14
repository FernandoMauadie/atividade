import listaG as L#import da função

print('1 - Salgado, 2 - Refrigerante, 3- Suco, 4 - Sorvete, 5 - Cafe , 6 - Capuccino , 7 - Bolo, 8 - Dadinho')#numero dos produtos
a = int(input('coloque o numero do produto'))#colocar o numero do produto
L.prod(a)#ultiliza a função prod com o parametro sendo a
print('valor do produto:',L.prod(a))#imprime o valor do produto
