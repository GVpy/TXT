nome = str(input("Digite o nome do produto: "))
valor = float(input("Digite o valor do produto: "))
quantidade = int(input("Digite a quantidade"))

arquivo = open("pessoa.txt", "a")
arquivo.write(f"{nome} |   {valor} |  {quantidade} \n")
arquivo.close