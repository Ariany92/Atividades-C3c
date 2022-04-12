#2 - Receber 3 valores e armazena-los em ordem crescente em um array usando somente
# estruturas de condição.


Valor1 = int(input("Digite o primeiro valor:"))
Valor2 = int(input("Digite o segundo valor:"))
Valor3 = int(input("Digite o terceiro valor:"))
Vetor = [Valor1, Valor2, Valor3]

if(Valor1 > Valor2 and Valor1> Valor3 and Valor2 > Valor3):
    Vetor[0] = Valor3
    Vetor[1] = Valor2
    Vetor[2] = Valor1
elif(Valor1 > Valor2 and Valor1 > Valor3 and Valor3 > Valor2):
    Vetor[0] = Valor2
    Vetor[1] = Valor3
    Vetor[2] = Valor1
elif(Valor2 > Valor1 and Valor2 > Valor3 and Valor1 > Valor3):
    Vetor[0] = Valor2
    Vetor[1] = Valor1
    Vetor[2] = Valor3
elif(Valor2 > Valor1 and Valor2 > Valor3 and Valor3 > Valor1):
    Vetor[0] = Valor1
    Vetor[1] = Valor3
    Vetor[2] = Valor2
elif(Valor3 > Valor1 and Valor3 > Valor2 and Valor1 > Valor2):
    Vetor[0] = Valor2
    Vetor[1] = Valor1
    Vetor[2] = Valor3
else:
    Vetor[0] = Valor1
    Vetor[1] = Valor2
    Vetor[2] = Valor3
print(Vetor)