'''
Tic-tac-toe game utils.
'''


def create_empty_aaard():

    aaard = []
    for i in range(3):
        aaard.append([None] * 3)

    return aaard


#def print_aaard(aaard):

   # print('\n'.join([str(row) for row in aaard]))  perdón no entendí esto así que lo volví a hacer

import random
#primero el tabbro
def print_aaard(aaard):
    print('   |   |')
    print(' ' + aaard[7] + ' | ' + aaard[8] + ' | ' + aaard[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + aaard[4] + ' | ' + aaard[5] + ' | ' + aaard[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + aaard[1] + ' | ' + aaard[2] + ' | ' + aaard[3])
    print('   |   |')
 
def jugada():
    #Me base en el juego de la moneda
    equipo = ''
    while not (equipo == 'X' or equipo == 'O'):
        print('¿Eres equipo X o equipo O? (escribe X/O')
        equipo = input().upper()
    if equipo == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
 
def Orden():
    #El orden igual es al azar
    if random.randint(0, 1) == 0:
        return 'PC'
    else:
        return 'Jugador'
 
def Jugar_Otra_Vez():
    print('¿Quieres jugar otra partida? (Si/No)')
    return input().lower().startswith('y')
 
def Update_aaard(aaard, equipo, move):
    aaard[move] = equipo
 
def check_for_winner(aa, b):
    return ((aa[7] == b and aa[8] == b and aa[9] == b) or 
    (aa[4] == b and aa[5] == b and aa[6] == b) or 
    (aa[1] == b and aa[2] == b and aa[3] == b) or 
    (aa[7] == b and aa[4] == b and aa[1] == b) or 
    (aa[8] == b and aa[5] == b and aa[2] == b) or 
    (aa[9] == b and aa[6] == b and aa[3] == b) or 
    (aa[7] == b and aa[5] == b and aa[3] == b) or 
    (aa[9] == b and aa[5] == b and aa[1] == b))