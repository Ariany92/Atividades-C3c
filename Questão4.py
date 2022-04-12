#4 - Receber o salário fixo e o valor das vendas efetuadas pelo vendedor de uma empresa.
# Sabendo-se que ele recebe uma comissão de 3% sobre o total das vendas até R$ 1.500,00
# mais 5% sobre o que ultrapassar este valor, calcular e escrever o seu salário total.


Salariofixo = float(input("Qual o salário fixo? "))
Valorvendas = float(input("Qual o valor de vendas? "))

if Valorvendas <= 1500:
    Comisao = Valorvendas * 0.03
    Salariototal = Salariofixo + Comisao
    print(f"O salário final é {Salariototal}")
else:
    Comisao = Valorvendas * 0.05
    Salariototal = Salariofixo + Comisao
    print(f"O salário final é :{Salariototal}")
