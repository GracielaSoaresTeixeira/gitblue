from uteis import Numeros
#Pgm principal
help(Numeros.fatorial)
num=int(input('Valor ==> '))
fat=Numeros.fatorial(num)
print(f'fatorial {num} = {fat}')
print(f'dobro    {num} = {Numeros.dobro(num)}')
print(f'triplo   {num} = {Numeros.triplo(num)}')
