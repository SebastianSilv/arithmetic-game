def modulo(num_1, num_2):
    if num_2 == 0:
        print("Error: No se puede calcular el módulo con el divisor cero.")
        return None
    resultado = num_1 % num_2
    print(f'{num_1} % {num_2} = {resultado}')
    return resultado