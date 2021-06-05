# Instalar separado no cmd
#pip install py_expression_eval

#pip install PySimpleGUI

#pip install PyInstaller
#py installer --windowed PO2_trabalho1.py

from PySimpleGUI import PySimpleGUI as sg
from py_expression_eval import Parser


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