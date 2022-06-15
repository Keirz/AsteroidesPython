x = qnt = soma = 0
x = int(input(print('Digite o numero [Digite 2555 para parar]')))
while x != 2555:
    soma += x
    qnt += 1
    x = int(input(print('Digite o numero [Digite 2555 para parar]')))
print(f"Voce digitou {qnt} números e a soma entre eles foi de {soma}")

