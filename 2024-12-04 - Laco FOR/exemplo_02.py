'''
   Faça um programa que solicite ao usuário um valor n inteiro positivo e 
   imprima os n primeiros trios de valores que formam um triângulo pitagórico.
'''
import sys

n = int(input("Digite o valor de n (número de trios): "))

if n <= 0:
   sys.exit('O número deve ser positivo...')
   
# Contador de trios encontrados
contador = 0  

# Começa com c = 5, que é o menor valor para o qual um triângulo pitagórico válido existe
lado_c = 5

while contador < n:
   for lado_a in range(1, lado_c):
      for lado_b in range(lado_a, lado_c):
         if lado_a**2 + lado_b**2 == lado_c**2:
            print(f'{lado_a}, {lado_b}, {lado_c}')
            contador += 1
            if contador == n: break
         if contador == n: break
   lado_c += 1
