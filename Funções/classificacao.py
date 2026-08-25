not1 = float(input("Digite a primeira nota do aluno: "))
not2 = float(input("Digite a segunda nota do aluno: "))
not3 = float(input("Digite a terceira nota do aluno: "))

media = (not1 + not2 + not3) / 3

print("\n")

if not1 < 4 or not2 < 4 or not3 < 4:
	print("Reprovado por nota menor que 4")
elif media > 7:
	print(f"Aprovado: média {media:.2f}")
elif media > 5:
	print(f"Recuperação: média {media:.2f}")
else:
	print(f"Reprovado: média {media:.2f}")