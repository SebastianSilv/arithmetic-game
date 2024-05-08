from suma import suma
from resta import resta
from multi import multiplicacion
from divicion import division
from potencia import potencia
from modulo import modulo

def game():
    score = 0
    while True:
        print('======== Menu ========')
        print('\n1. Jugar')
        print('\n0. Exit')
        option = int(input('\nChoice an option: '))
        if option == 0:
            break
        num_1 = int(input('Enter first number: '))
        num_2 = int(input('Enter second number: '))


        answerS = int(input('Enter your answer for Suma: '))
        resultS = suma(num_1, num_2)
        if resultS == answerS:
            score += 1
            print('Correct for suma!')
        else:
            print('Incorrect for suma')

        answerR = int(input('Enter your answer for Resta: '))
        resultR = resta(num_1, num_2)
        if resultR == answerR:
            score += 1
            print('Correct for Resta!')
        else:
            print('Incorrect for resta')

        answerM = int(input('Enter your answer for multiplicacion: '))
        resultM = multiplicacion(num_1, num_2)
        if resultM == answerM:
            score += 1
            print('Correct for multiplicacion')
        else:
            print('Incorrect for multiplicacion')

        answerD = int(input('Enter your answer for division: '))
        resultD = division(num_1, num_2)
        if resultD is not None and resultD == answerD:
            score += 1
            print('Correct for division!')
        else:
            print('Incorrect for division')

        answerP = int(input('Enter your answer for potencia: '))
        resultP = potencia(num_1, num_2)
        if resultP == answerP:
            score += 1
            print('Correct for potencia!')
        else:
            print('Incorrect for potencia')

        answerO = int(input('Enter your answer for modulo: '))
        resultO = modulo(num_1, num_2)
        if resultO is not None and resultO == answerO:
            score += 1
            print('Correct for modulo!')
        else:
            print('Incorrect for modulo')
            
        
        print(f'======== Game Over ========')
        print(f'\nYour score is {score}')
        print('Keep going!')
        
game()