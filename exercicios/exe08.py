# Peça um valor em reais e mostre quantos dólares (considere US$1 = R$5,00) você pode comprar.

valor_reais = float(input('Digite quanto voce tem em R$: '))
dolar = valor_reais / 5.00

print(f'Com R${valor_reais}, voce comprará US${dolar}')