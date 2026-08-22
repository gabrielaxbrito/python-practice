valores = [100,50,20,10,5,2]
quantidades = []

saque = int(input("Digite o valor que deseja sacar: ")) 

for valor in valores:
	qtd = int(input(f"Quantidade de notas de {valor}: "))
	quantidades.append(qtd) #irá colocar o que foi recebido na lista

usadas = [] #vai me dizer quantas notas foram usadas no saque

restante = saque #restante vai diminuindo a cada nota usada

for i in range(len(valores)):
	nota_usa = restante // valores[i]
	if nota_usa > quantidades[i]:
		nota_usa = quantidades[i]
	usadas.append(nota_usa) #Vai guardando quantas notas de cada tipo foi usada
	restante -= nota_usa * valores[i]

if restante == 0:
	print("Saque bem sucedido!")
	for i in range(len(valores)):
		if usadas[i] > 0:
			print(f"Notas de {valores[i]}: {usadas[i]}")
else:
	print("Não foi possível realizar o saque com as notas disponíveis.")