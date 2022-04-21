import hashlib

def usuario(Email,Senha):

    Dados = {

        "ariany@gmail.com" : "abc012",
        "maria@outlook.com" : "1234dce",
        "jose@gmail.com" : "a1b2c3d"
    }

    Codificacao = hashlib.md5(Senha.encode()).digest()

    if Email in Dados and Codificacao == hashlib.md5(Dados[Email] .encode()).digest():
        return True
    elif Email not in Dados:
        return "Usuário não Cadastrado"
    else:
        return False

