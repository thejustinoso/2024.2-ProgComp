'''
   EXEMPLO 05:
   Fazer um programa em que o usuário informe uma frase e depois uma palavra
   e em seguida o programa informe se a palavra informada está na string informada
'''

# Solicita ao usuário que informe uma frase
frase = input('Informe uma frase: ')

# Solicita ao usuário que informe uma palavra
palavra = input('Informe uma palavra: ')

# Verifica se a palavra está na string
if palavra in frase:
   print('A palavra está na string.')
else:
   print('A palavra não está na string.')