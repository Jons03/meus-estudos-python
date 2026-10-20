nota = float(input('Digite sua nota: '))

if nota < 0 or nota > 10:
  print ('Nota inválida')
elif nota >= 7:
  print ('Apovado')
elif nota >= 5:
  print ('Recuperação')
else:
  print ('Reprovado')
