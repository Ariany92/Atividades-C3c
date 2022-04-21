import Usuários

entrada = ""
contagem = 0

while entrada != "n":
  Email = input("Digite seu email: ")
  Senha = input("Digite sua senha: ")
  if Usuários.usuario(Email,Senha) == True:
     print ("Login feito com sucesso")
     break
  elif Usuários.usuario(Email,Senha) == False:
        print("Dados não cadastrados no sistema. Realize seu cadastro")
  else:
      print("Dados incorretos, digite novamente")
      contagem += 1
      if contagem == 3:
         print("Número de tentativas Excedido. Seu cadastro está bloqueado.")
         break
  entrada = input("Deseja acessar o sistema? Digite s ou n ")