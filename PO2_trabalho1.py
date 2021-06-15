# Instalar separado no cmd
#pip install py_expression_eval

#pip install PySimpleGUI

#pip install PyInstaller
#py installer --windowed PO2_trabalho1.py

from PySimpleGUI import PySimpleGUI as sg
from py_expression_eval import Expression, Parser
import math


# Define conteudo da janela
sg.theme('Reddit')
layout = [  [sg.Text('Expressão:'), sg.Input(key='expressao')],
            [sg.Text('x:'), sg.Input(key='variavel')],
            [sg.Text('delta:'), sg.Input(key='delta')],
            [sg.Button('Ok')],
            [sg.Text('', justification='center', key='resultado', size=(10, 2))] ]


#   Rotina: Método Busca Uniforme
f = []      # vetor do f(x)
y = []      # vetor do x
# pra testar só trocar o a e b
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
#   Rotina: Método de Busca Docotômica - giu

#   Rotina: Método da Seção Áurea
def SecaoAurea(a,b,epsilon):
    alfa = (-1 + math.sqrt(5))/2
    beta = 1 - alfa
    k = 0
    
    dif = b-a
    m = a + beta * dif
    l = a + alfa * dif
    
    while (b-a) >= epsilon:
        k += 1
        
        fl = parser.parse(valores['expressao']).evaluate({'x': l})
        fm = parser.parse(valores['expressao']).evaluate({'x': m})
        
        if fm > fl:
            a = m
            m = l
            l = a + alfa * (b-a)
        else:
            b = l
            l = m
            m = a + beta * (b-a)
        
    x = (a+b)/2
    k += 1
    print("X* = %.4f" % x)
    print("k variando de 1 a %d" % k)

#   Rotina: Método de Fibonacci
def Fibonacci(a,b,epsilon):
    Fn = (b-a)/epsilon
    
    F = []
    
    F.append(1)
    F.append(1)
    
    N = 1
    
    while F[N] <= Fn:
        N = N+1
        F.append(F[N-1] + F[N-2])
        
    k = 0
    
    m = a + F[N-2]/F[N] * (b-a)
    l = a + F[N-1]/F[N] * (b-a)
    
    
    #print(N)
    for k in range(1, N-2):
        fm = parser.parse(valores['expressao']).evaluate({'x': m})
        fl = parser.parse(valores['expressao']).evaluate({'x': l})
        
        if fm > fl:
                a = m
                m = l
                
                l = a + (F[N-k-1])/F[N-k] * (b-a)
        else:
                b = l
                l = m
                
                m = a + (F[N-k-2])/F[N-k] * (b-a)
    x = (a+b)/2
    k += 1
    print("X* = %.4f" % x)
    print("k variando de 0 a %d" % k)

#   Rotina: Método da Bisseão - Giu


#   Rotina: Método de Newton  

# Cria janela
janela = sg.Window('PO2 - Trabalho 1', layout)

parser = Parser()

while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Ok':
        x = float(valores['variavel'])
        delta = float(valores['delta'])
        atualizarResultado = str(parser.parse(valores['expressao']).evaluate({'x': x}))
        print(atualizarResultado)
        janela['resultado'].update('Resultado: ' + atualizarResultado)

        # Testes
        #BuscaUniforme(-1,6,delta,atualizarResultado)
        #passei delta como epsilon
        #SecaoAurea(0.5,2.5,delta)
        #Fibonacci(0.5,2.5,delta)
