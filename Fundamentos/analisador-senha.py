#string iterável
senha = input("Digite uma senha para ser avaliada: ")

cont = 0
cont_letra = 0
cont_digito = 0
cont_especial = 0

for i in senha:
    cont=cont + 1
    if i.isalpha(): ##verifica se o caractere é uma letra, se sim return True
        cont_letra = cont_letra + 1
    elif i.isdigit(): ##verifica se o caractere é um dígito, se sim return True
        cont_digito = cont_digito + 1
    else:
        cont_especial = cont - (cont_letra + cont_digito)

print(f"A senha contém {cont} caractere(s)")
print(f"A senha contém {cont_letra} letra(a)")
print(f"A senha contém {cont_digito} digíto(s)")
print(f"A senha contém {cont_especial} caractere(s) especial(is)")


if cont < 6 or cont_digito == 0 or cont_especial == 0:
    print("A senha é fraca") # se possui menos de 6 caracteres ou não possui dígito ou não possui caractere especial

elif cont >= 10 and cont_digito >= 2 and cont_especial >= 2 and cont_letra >= 3:
    print("A senha é forte") # 10 ou mais caracteres, pelo menos 2 digítos, pelo menos 2 caracteres especiais e pelo menos 3 letras

else:
    print("A senha é média")

