# def soma():
#     return 1 + 4

# resultado = soma()
# print(resultado)

def soma(a: int, b: int) -> int:
    """Soma dois numeros inteiros 

    Args:
        a (int): numero inteiro
        b (int): numero inteiro

    Returns:
        int: numero inteiro
    """
    result = a + b
    print(result)
    return result
    

resultado = soma(1, 2)
print(soma.__doc__) # como usar a documentação sem IDE
print(resultado)
