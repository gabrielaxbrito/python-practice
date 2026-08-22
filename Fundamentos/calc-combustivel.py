dist_percorrida = float(input("Digite a distância percorrida pelo veículo (km): "))
consumo = float(input("Digite o consumo do veículo (km/l): "))
valor = float(input("Digite o preço do combustível (R$): "))


litros_ult =  dist_percorrida * consumo
custo = litros_ult * valor
custo_km = custo / dist_percorrida

print(f"Litros utilizados na viagem: {litros_ult}")
print(f"Custo total do abastecimento: {custo}")
print(f"Valor gasto por KM rodado: {custo_km}")

print("---------------------------------------------------\n\n")

print("SEGUNDA VIAGEM")

dist_percorrida2 = float(input("Digite a distância percorrida pelo veículo (km): "))
consumo2 = float(input("Digite o consumo do veículo (km/l): "))
valor2 = float(input("Digite o preço do combustível (R$): "))


litros_ult2 =  dist_percorrida2 * consumo2
custo2 = litros_ult2 * valor2
custo_km2 = custo2 / dist_percorrida2

print(f"Litros utilizados na viagem: {litros_ult2}")
print(f"Custo total do abastecimento: {custo2}")
print(f"Valor gasto por KM rodado: {custo_km2}")

if custo_km < custo_km2:
    print("A primeira viagem foi mais econômica")
elif custo_km > custo_km2:
    print("A segunda viagem foi mais econômica")
else:
    print("As duas viagens tiveram o mesmo custo por km rodado")
