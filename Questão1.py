#1 - Receber as notas da 1a. e 2a. avaliações de um aluno. Calcular a média aritmética
# simples e escrever uma mensagem que diga se o aluno foi ou não aprovado
# (considerar que nota igual ou maior que 7 o aluno é aprovado). Escrever também a
# média calculada. Obs.: Utilizar dicionários para armazenas os valores.


Nota1 = float(input("Digite a primeira nota:"))
Nota2 = float(input("Digite a segunda nota:"))

Media = (Nota1 + Nota2)/2

print(f"A media aritimética do aluno foi {Media}")
if(Media >= 7):
      print("Aluno aprovado")
else:
      print("Aluno reporvado")