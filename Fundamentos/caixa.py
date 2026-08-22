valor = int(input("Digite o valor: "))


# if valor == 5:
#     print("Irá precisa de 1 nota de 5")
# elif valor == 10:
#     print("Irá precisa de 1 nota de 10")
# elif valor == 20:
#     print("Irá precisa de 1 nota de 20")
# elif valor == 50:
#    print("Irá precisa de uma nota de 50") 
# elif valor == 100:
#     print("Irá precisar de 1 nota de 100")

mod = valor % 100
res = valor // 100

mod2 = mod % 50
res2 = mod //50

mod3 = mod2 % 20
res3 = mod2 // 20

mod4 = mod3 % 10
res4 = mod3 // 10    

mod5 = mod4 % 5
res5 = mod4 // 5 

print(f"Irá precisade de: \n {res} notas de R$100,00 \n {res2} notas de R$50,00 \n {res3} notas de R$20,00 \n {res4} notas de R$10,00 \n {res5} notas de R$5,00")

print("---------------------------------------------------\n\n")

reais = [100, 50, 20, 10, 5]

for  real in reais:
	
	mod = valor % real
	res = valor // real
	
	print(f"{res} nota(s) de {real}")
	valor = mod
