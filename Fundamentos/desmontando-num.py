num = input("Digite um valor: ")

medidas = ["unidade", "dezena", "centena", "milhar", "dezena de milhar"]

cont = 0

for i in num:
    if i.isdigit():
        cont = cont + 1
print("\n")
print(f"O número possúi {cont} ordens numéricas.")
print("\n")
 ##Consigo saber quantas ordens numéricas há no número digitado.
if cont == 1:
    print(f"O número só possúi uma unidade: {num}")
elif cont == 2:
    print(f"O número possúi uma unidade e uma dezena")
elif cont == 3:
    print(f"O número possúi uma unidade, uma dezena e uma centena")
elif cont == 4:
    print(f"O número possúi uma unidade, uma dezena, uma centena e um milhar")
elif cont == 5:
    print(f"O número possúi uma unidade, uma dezena, uma centena, um milhar e uma dezena de milhar")

##consigo saber quais são as ordens numéricas do número digitado.
print("\n\n")
print("As ordens numéricas do número digitado são: ")
print("\n")
num2 = int(num)

for i in range(len(medidas)):

    mod = num2 % 10
    quociente = num2 // 10

    print(f"{medidas[i]}: {mod}")

    num2 = quociente