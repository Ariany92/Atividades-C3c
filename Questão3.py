#3 - Receber a hora de início e a hora de fim de um jogo de Xadrez
# (considere apenas horas inteiras, sem os minutos) e calcule a duração do jogo em horas,
# sabendo-se que o tempo máximo de duração do jogo é de 24 horas e que o jogo pode iniciar
# em um dia e terminar no dia seguinte.

from math import fabs

IniciodoJogo = int(input("Digite a hora em que começou o jogo:"))
TerminoJogo = int(input("Digite a hora que terminou o jogo:"))
DuracaodoJogo = fabs(TerminoJogo - IniciodoJogo)

print(f"A partida durou {DuracaodoJogo} horas")
