# Abre em modo de somente Leitura.
f  = open("test.txt", "r")
print(f.read())
f.close()

# Abre em modo de Escrita substituindo o seu conteúdo anterior
f = open("test.txt","w")
f.write("This text will overwrite the content of our file.")
f = open("test.txt")
print(f.read())
f.close()

# insere em nova linha
f=open("test.txt","a")
f.write("\nThis text will be appended to the file")
f = open("test.txt")
print(f.read())

# Cria um novo arquivo, qdo o arquivo não existe
f=open("test2.txt", "x")
f.write("\nThis text will be appended to the file.")

f=open("test2.txt")
print(f.read())
f.close()
