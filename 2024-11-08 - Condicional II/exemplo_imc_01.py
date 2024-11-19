import sys

peso = float(input('Informe o peso (kg)...: '))
if peso <= 0:
    sys.exit('Peso Inválido...\nO peso tem de ser positivo!!!')

altura = float(input('Informe sua altura (m): '))
if altura <= 0:
    sys.exit('Altura Inválida...\nA altura tem de ser positiva!!!')

imc = round(peso / (altura**2), 1)
print(f'IMC = {imc}')

if imc < 18.5:
    print('Abaixo do Peso ...')
elif imc <= 24.9:
    print('Peso Normal ...')
elif imc <= 29.9:
    print('Sobrepeso ...')
elif imc <= 34.9:
    print('Obesidade Grau I ...')
elif imc <= 39.9:
    print('Obesidade Grau II ...')
else:
    print('Obesidade Grau III (Mórbida)...')