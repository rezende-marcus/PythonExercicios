salario = float(input('Qual é o salario do Funcionario? R$'))
novo = salario +(salario * 15 / 100)
print('Salario de R${:.2f} com 15% de aumento é R${:.2f}'.format(salario, novo))