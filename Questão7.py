#7 - Escreva um código que receba as idades de 2 homens e de 2 mulheres
# (considere que as idades dos homens serão sempre diferentes entre si, bem como as das mulheres).
# Calcule e escreva a soma das idades do homem mais velho com a mulher mais nova,
# e o produto das idades do homem mais novo com a mulher mais velha.


Homem1 = int(input("Idade do primeiro homem: "))
Homem2 = int(input("Idade do segundo homem: "))
Mulher1 = int(input("Idade da primeira mulher: "))
Mulher2 = int(input("Idade da segunda mulher: "))

if Homem1 == Homem2 or Mulher1 == Mulher2 or Homem1 == Homem2 and Mulher1 == Mulher2:
    print("Digite idades diferentes!!!")
elif Homem1 > Homem2 and Mulher1 > Mulher2:
    Soma = Homem1 + Mulher2                  #SOMA Homem mais VELHO com mulher mais NOVA#
    Produto = Homem2*Mulher1                 #PRODUTO Homem mais NOVO com mulher mais VELHA#
elif Homem1 > Homem2 and Mulher2 > Mulher1:
    Soma = Homem1 + Mulher1
    Produto = Homem2 * Mulher2
elif Homem2 > Homem1 and Mulher2 > Mulher1:
    Soma = Homem2 + Mulher1
    Produto = Homem1 * Mulher2
elif Homem2 > Homem1 and Mulher1 > Mulher2:
    Soma = Homem2 + Mulher2
    Produto = Homem1 * Mulher1


print(f"Soma das idades homem mais velho + mulher mais nova é {Soma} e o produto das idades do homem "
      f"mais novo X mulher mais velha é {Produto}")
