# Instalar separado no cmd
#pip install py_expression_eval

#pip install PySimpleGUI

#pip install PyInstaller
#py installer --windowed PO2_trabalho1.py

from PySimpleGUI import PySimpleGUI as sg
from py_expression_eval import Expression, Parser


# Define conteudo da janela
sg.theme('Reddit')
layout = [  [sg.Text('Expressão:'), sg.Input(key='expressao')],
            [sg.Text('x:'), sg.Input(key='variavel')],
            [sg.Button('Ok')],
            [sg.Text('', justification='center', key='resultado', size=(10, 2))] ]

# Cria janela
janela = sg.Window('PO2 - Trabalho 1', layout)

parser = Parser()

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Ok':
        x = float(valores['variavel'])
        atualizarResultado = str(parser.parse(valores['expressao']).evaluate({'x': x}))
        print(atualizarResultado)
        janela['resultado'].update('Resultado: ' + atualizarResultado)

#   Rotina: Método Busca Uniforme - Funcionando
f = []      # vetor do f(x)
y = []      # vetor do x
def BuscaUniforme(a,b,delta,atualizarResultado):
    x = a
    ok = False
    while x <= b:
        y.append(x)
        atualizarResultado = str(parser.parse(valores['expressao']).evaluate({'x': x}))
        f.append(float(atualizarResultado))
        x = x + delta
        if len(y) > 1 and len(f) > 1:                
            if(f[len(f)-1] > f[len(f)-2]) and (ok == False):
                ok = True
                # Refinamento - depois tentar colocar em uma rotina separada
                y.pop()
                y.pop()
                f.pop()
                f.pop()
                x = y[len(y)-1]
                delta = delta / 10    
            if(f[len(f)-1] > f[len(f)-2]) and (ok == True):
                break
    print("X* = %4f" % y[len(y)-2])

