#5 - Faça um código que receba: quantidade atual em estoque, quantidade máxima em estoque
# e quantidade mínima em estoque de um produto. Calcular e escrever a quantidade média
# ((quantidade média = quantidade máxima + quantidade mínima)/2).
# Se a quantidade em estoque for maior ou igual a quantidade média escrever a
# mensagem 'Não efetuar compra', senão escrever mensagem 'Efetuar compra'

Quantidadeestoque = int(input("Quantidade atual em estoque:"))
Quantidademaxima = int(input("Quatidade máxima em estoque:"))
Quantidademinima = int(input("Quantidade mínima em estoque:"))

Quantidademedia = (Quantidademaxima + Quantidademinima)/2
print(f"A quantidade média do estoque é {Quantidademedia}")

if Quantidadeestoque >= Quantidademedia:
    print("Não efetuar compra")
else:
    print("Efetuar compra")