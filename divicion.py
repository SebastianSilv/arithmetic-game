def division(num_1, num_2):
    if num_2 == 0:
        print("Error: No se puede dividir entre cero.")
        return None
    resultado = num_1 / num_2
    print(f'{num_1} / {num_2} = {resultado}')
    return resultado