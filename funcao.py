
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
bloqueados = {}     
                                                             # Guarda o tempo de desbloqueio de cada usuário.

def cadastrar(nome,data_nascimento,email, senha,):
    with open("usuarios.json", "r") as f:                 # Abre o arquivo no modo de leitura.
        usuarios = json.load(f)                           # Converte o conteúdo do JSON para um dicionário Python.

    if email in usuarios:                               # Verificar se o usuário já existe
        print("Usuário já existe.")                       # Isso impede que o mesmo nome de usuário seja usado duas vezes.
        return False

    usuarios[email] = [nome,data_nascimento,senha,]                           # Isso adiciona a nova entrada no dicionário: {"usuario": "senha"}

    with open("usuarios.json", "w") as f:                 # Aqui salva novamente no arquivo JSON
        json.dump(usuarios, f)                            # Agora o dicionário atualizado é salvo no arquivo usuarios.json.

    print("Cadastro realizado com sucesso!")              # Mostra a mensagem e retorna
    return True 

def login(email, senha):
    # Verifica se o usuário está bloqueado
    if email in bloqueados:
        tempo_restante = int(bloqueados[email] - time.time())
        if tempo_restante > 0:
            print(f"Tentativas excedidas. Espere {tempo_restante} segundos.")
            return False
        else:
            # Desbloqueia após o tempo passar
            del bloqueados[email]
            tentativas[email] = 0

    with open("usuarios.json", "r") as f:                  # Igual ao cadastro: lê os dados salvos.
        usuarios = json.load(f)

    if email in usuarios and usuarios[email][2] == senha:          # Verifica se o usuário existe e a senha está correta
        print("Login realizado com sucesso!")
        tentativas[email] = 0  # zera erros
        
        return True
    else:
        # Registra tentativa
        tentativas[email] = tentativas.get(email, 0) + 1
        print("Usuário ou senha incorretos.")

        if tentativas[email] >= 3:
            bloqueados[email] = time.time() + 30  # 30 segundos
            print("Você errou 3 vezes. Espere 30 segundos para tentar novamente.")

        return False

def cadastro_livro(titulo,autor, genero,classificacao):
    with open("livro.json", "r") as f:                 # Abre o arquivo no modo de leitura.
        livros = json.load(f)                           # Converte o conteúdo do JSON para um dicionário Python.

    if titulo in livros:                               # Verificar se o usuário já existe
        print("livro já existe.")                       # Isso impede que o mesmo nome de usuário seja usado duas vezes.
        return False

    livros[titulo] = [autor,genero,classificacao]                           # Isso adiciona a nova entrada no dicionário: {"usuario": "senha"}

    with open("livro.json", "w") as f:                 # Aqui salva novamente no arquivo JSON
        json.dump(livros, f)                            # Agora o dicionário atualizado é salvo no arquivo usuarios.json.

    print("Cadastro realizado com sucesso!")              # Mostra a mensagem e retorna
    return True 

def exibir_livros():
    with open("livro.json", "r") as f:                 # Abre o arquivo no modo de leitura.
        livros = json.load(f)                           # Converte o conteúdo do JSON para um dicionário Python.
    print(livros)

# Teste simples via terminal


logado = False
print("1 - Cadastrar\n2 - Login")
op = input("Escolha uma opção: ")

 
if op == "1":
    nome = input("Nome: ")
    email = input("E-mail: ")
    data_nascimento = input("Data de Nascimento: ") 
    senha = input("Senha: ")
    categroia = input("Categoria[autor, leitor]: ")
    cadastrar(nome,data_nascimento,email, senha,)
elif op == "2":
    email = input("E-mail: ")
    senha = input("Senha: ")
    logado = login(email, senha)
    print("Bem Vindo a Biblioteca")
elif op == "sair":
    print("Saindo...")
         
else:
    print("Opção inválida.")

if logado:
    print("O que deseja fazer?")
    print("1 - Ver Livros")
    print("2 - adcionar um Livro")
    print("3 - editar perfil")
    print("4 - sair")
   
    op = input("Escolha uma opção: ")
    if op == "1":
        exibir_livros()
    elif op == "2":
        titulo = input("Titulo: ")
        autor = input("Autor: ")
        genero = input("Genero: ")
        classificacao = input("Classificação: ")
        cadastro_livro(titulo,autor,genero,classificacao)
        print("Livro adicionado")
    elif op == "3":
        print("Perfil editado")
    elif op == "4":
        print("Saindo...")
    else:
        print("Opção inválida.")

