livros = {
  'Nome:': "Livro 1",
  'Autor:': "Autor 1",
  'categoria': "terror",
}



#funcao para adicionar um livro
def adicionar_livro(nome, autor, categoria):
  livros['Nome:'] = nome
  livros['Autor:'] = autor
  livros['categoria'] = categoria


adicionar_livro('Livro 2', 'Autor 2', 'Romance')
print(livros)


# Função Cadastrar e Login:

import json
import os
import time

# Verifica se o arquivo de usuários existe
if not os.path.exists("usuarios.json"):                   
    with open("usuarios.json", "w") as f:
        json.dump({}, f)

# Dicionários para controle interno
tentativas = {}                                           # Guarda o número de tentativas erradas de cada usuário.
bloqueados = {}                                           # Guarda o tempo de desbloqueio de cada usuário.

def cadastrar(usuario, senha):
    with open("usuarios.json", "r") as f:                 # Abre o arquivo no modo de leitura.
        usuarios = json.load(f)                           # Converte o conteúdo do JSON para um dicionário Python.

    if usuario in usuarios:                               # Verificar se o usuário já existe
        print("Usuário já existe.")                       # Isso impede que o mesmo nome de usuário seja usado duas vezes.
        return False

    usuarios[usuario] = senha                             # Isso adiciona a nova entrada no dicionário: {"usuario": "senha"}

    with open("usuarios.json", "w") as f:                 # Aqui salva novamente no arquivo JSON
        json.dump(usuarios, f)                            # Agora o dicionário atualizado é salvo no arquivo usuarios.json.

    print("Cadastro realizado com sucesso!")              # Mostra a mensagem e retorna
    return True 

def login(usuario, senha):
    # Verifica se o usuário está bloqueado
    if usuario in bloqueados:
        tempo_restante = int(bloqueados[usuario] - time.time())
        if tempo_restante > 0:
            print(f"Tentativas excedidas. Espere {tempo_restante} segundos.")
            return False
        else:
            # Desbloqueia após o tempo passar
            del bloqueados[usuario]
            tentativas[usuario] = 0

    with open("usuarios.json", "r") as f:                  # Igual ao cadastro: lê os dados salvos.
        usuarios = json.load(f)

    if usuario in usuarios and usuarios[usuario] == senha:          # Verifica se o usuário existe e a senha está correta
        print("Login realizado com sucesso!")
        tentativas[usuario] = 0  # zera erros
        return True
    else:
        # Registra tentativa
        tentativas[usuario] = tentativas.get(usuario, 0) + 1
        print("Usuário ou senha incorretos.")

        if tentativas[usuario] >= 3:
            bloqueados[usuario] = time.time() + 30  # 30 segundos
            print("Você errou 3 vezes. Espere 30 segundos para tentar novamente.")

        return False


# Teste simples via terminal
print("1 - Cadastrar\n2 - Login")
op = input("Escolha uma opção: ")

usuario = input("Usuário: ")
senha = input("Senha: ")

if op == "1":
    cadastrar(usuario, senha)
elif op == "2":
    login(usuario, senha)
else:
    print("Opção inválida.")




