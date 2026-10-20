nome = input('Digite o seu nome: ')
print ('Olá, prazer em conhecer', nome)

idade = int(input('Quantos anos você tem?'))
if idade > 18:
  print ('Você é de maior')
elif idade == 18:
  print ('Pessoa com exatamente 18 anos')
else:
  print ('Você é de menor')

