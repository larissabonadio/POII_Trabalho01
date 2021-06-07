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


#   Teste: Método Busca Uniforme
a = 0.5
b = 2.5
delta = 0.6
f = []
y = []
i = 0
x = a
n = 2   
# x^2-3*x+2
# 2 primeiros valores serão guardos em um vetor para comparação
while x <= b:
    
    if len(f) < 2:
        for i in range(0, n):
            y.append(x)
            atualizarResultado = str(parser.parse(valores['expressao']).evaluate({'x': x}))
            f.append(float(atualizarResultado))
            x = x + delta
    else:
        n = len(f)
        if (f[n-1] > f[n-2]): 
            break
            # refinamento
        else:
            y.append(x)
            atualizarResultado = str(parser.parse(valores['expressao']).evaluate({'x': x}))
            f.append(float(atualizarResultado))
            x = x + delta
    print(y)
    print(f)