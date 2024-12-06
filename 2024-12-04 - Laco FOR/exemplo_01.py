'''
   Faça um programa que solicite um valor n inteiro positivo e 
   imprima na tela o seguinte padrão:

   para n = 4

   o programa deverá imprimir

   1
   2 2
   3 3 3
   4 4 4 4
'''
import sys

n = int(input("Digite um valor inteiro positivo: "))

if n <= 0:
   sys.exit('O número deve ser positivo...')

for i in range(n + 1):
   print(f'{i} ' * i)