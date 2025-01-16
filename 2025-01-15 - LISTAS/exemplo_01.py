nomes = list()

while True:
   nome = input('Digite um nome ou "FIM" para encerrar:').upper()
   if nome == "FIM":
      break
   nomes.append(nome)

if not nomes
   print ('Nenhum nome foi digitado')
else:
   pesquisaNome = input('Digite um nome para ser pesquisado')
   if pesquisaNome in nomes:
      print(f'O nome {pesquisaNome} consta na lista de digitados')
   else:
      print(f'O nome {pesquisaNome} não consta na lista de digitados')
