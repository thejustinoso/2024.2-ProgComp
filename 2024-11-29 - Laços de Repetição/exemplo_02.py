'''
   Fazer um programa que fique lendo números inteiros solicitados ao usuário.

   Quando o usuário digitar 0, o programa deve finalizar e imprimir a soma de 
   todos os números digitados bem como a média aritmética.

   O valor 0 não deve entrar na média.
'''

intSoma = 0
intQtd  = 0

while True:
   n = int(input('Digite um número inteiro: '))

   if n == 0: break

   intSoma += n
   intQtd  += 1

print(f'A soma dos números digitados é {intSoma}')
print(f'A média aritmética dos números digitados é {intSoma/intQtd}')

