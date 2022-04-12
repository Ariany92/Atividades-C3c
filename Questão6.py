#Quais os valores serão armazenados em "z" e "resposta" para as seguintes situações:
#a) x = 5 e y = 10
#b) x = 200 e y = 100
#c) x = 27 e y = -34
#d) x = -8 e y =40
#e) x = 50 e y = 3


x = int(input("Digite um número x: "))
y = int(input("digite um outro número y: "))
z = (x*y)+5
if z <= 0:
    resposta = "A"
elif z <= 100:
    resposta = "B"
else:
    resposta = "C"
print("Resultado final: %i. Resposta: %s" %(z,resposta))