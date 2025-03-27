# numeros = [1, 2, 3, 5, 4, 6, 10, 8, 9, 7]

# print(numeros)
# print(numeros[-1])
# numeros.append(11)
# print(numeros)
# numeros.sort(reverse=True)
# print(numeros)

# numeros = (1, 2, 3, 5, 4, 6, 10, 8, 9, 7, 5)

# print(numeros)
# print(numeros.index(5))
# print(numeros.count(5))

numeros = {'um': 1, "dois": 2, "tres": 3}
# print(numeros.keys())
# print(numeros.values())
# print(numeros.get("um"))
# print(numeros["um"])
# print(numeros.get("cem", ""))

# del numeros["dois"]
numeros.pop("dois", "Não encontrado")
print(numeros)