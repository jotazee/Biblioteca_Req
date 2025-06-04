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



