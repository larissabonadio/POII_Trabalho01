import PySimpleGUI as sg
from sympy.polys.polyoptions import Symbols
from py_expression_eval import Expression, Parser
from sympy import *
import math

sg.theme('LightBrown13')

def window_buscaUniforme():
    layout = [[sg.Text('BUSCA UNIFORME', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Seja o intervalo a <= x <= b, insira:',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('Valor de a:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_a', size=(10,1))],
            [sg.Text('Valor de b:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_b', size=(10,1))],
            [sg.Text('Δ = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='delta', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaUniforme1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaUniforme2', text_color = 'black')]
            ]
    return sg.Window('Busca Uniforme', layout, size=(400, 400), finalize=True, resizable=True)

def window_buscaDicotomica():
    layout = [[sg.Text('BUSCA DICOTÔMICA', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Seja o intervalo a <= x <= b, insira:',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('Valor de a:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_a', size=(10,1))],
            [sg.Text('Valor de b:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_b', size=(10,1))],
            [sg.Text('Δ = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='delta', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaDicotomica1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaDicotomica2', text_color = 'black')]
            ]
    return sg.Window('Busca Dicotômica', layout, size=(400, 400), finalize=True, resizable=True)

def window_secaoAurea():
    layout = [[sg.Text('SEÇÃO ÁUREA', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Seja o intervalo a <= x <= b, insira:',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('Valor de a:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_a', size=(10,1))],
            [sg.Text('Valor de b:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_b', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaAurea1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaAurea2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaAurea3', text_color = 'black')]
            ]
    return sg.Window('Seção Áurea', layout, size=(400, 400), finalize=True, resizable=True)

def window_buscaFibonacci():
    layout = [[sg.Text('BUSCA FIBONACCI', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Seja o intervalo a <= x <= b, insira:',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('Valor de a:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_a', size=(10,1))],
            [sg.Text('Valor de b:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_b', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaFibonacci1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaFibonacci2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaFibonacci3', text_color = 'black')]
            ]
    return sg.Window('Busca Fibonacci', layout, size=(400, 400), finalize=True, resizable=True)

def window_bissecao():
    layout = [[sg.Text('MÉTODO DA BISSEÇÃO', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Seja o intervalo a <= x <= b, insira:',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('Valor de a:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_a', size=(10,1))],
            [sg.Text('Valor de b:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_b', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaBissecao1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaBissecao2', text_color = 'black')]
            ]
    return sg.Window('Bisseção', layout, size=(400, 400), finalize=True, resizable=True)

def window_newton():
    layout = [[sg.Text('MÉTODO DE NEWTON', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text('         ')],
            [sg.Text('Insira a função:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='expressao', size=(30,1))],
            [sg.Text('Seja o intervalo a <= x <= b, insira:',  font=('Arial', 10, 'bold'), text_color = 'black')],
            [sg.Text('Valor de a:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_a', size=(10,1))],
            [sg.Text('Valor de b:',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='valor_b', size=(10,1))],
            [sg.Text('ε = ',  font=('Arial', 10, 'bold'), text_color = 'black'), sg.Input(key='epsilon', size=(10,1))],
            [sg.Text('         ')],
            [sg.Button('Calcular', size=(15,1)), sg.Button('Sair', size=(15,1))],
            [sg.Text('         ')],
            [sg.Text(size=(40,1), key='respostaNewton1',  font=('Arial', 11, 'bold'))],
            [sg.Text(size=(40,1), key='respostaNewton2', text_color = 'black')]
            ]
    return sg.Window('Newton', layout, size=(400, 400), finalize=True, resizable=True)

# Janela Inicial Principal
def main_window():
    layout = [[sg.Text(' ', size = (10, 1))],
            [sg.Text('Selecione a rotina que deseja utilizar:', justification='center', font=('Arial', 11, 'bold'), text_color = '#921224')],
            [sg.Text(' ', size = (4, 1))],
            [sg.Button('Busca Uniforme', size=(20,1))],
            [sg.Button('Busca Dicotômica', size=(20,1))],
            [sg.Button('Seção Áurea', size=(20,1))],
            [sg.Button('Busca Fibonacci', size=(20,1))],
            [sg.Button('Bisseção', size=(20,1))],
            [sg.Button('Newton', size=(20,1))],
            [sg.Text(' ', size = (4, 1))],
            [sg.Button('Sair')]]
    return sg.Window('PO II - Trabalho 1', layout, size=(400, 400), element_justification='center', finalize=True, resizable=True)

#Metodo Busca Uniforme
def BuscaUniforme(a,b,delta,atualizarResultado, funcao):
    f = []      # vetor do f(x)
    y = []      # vetor do x
    x = a
    ok = False
    while x <= b:
        y.append(x)
        atualizarResultado = str(parser.parse(funcao).evaluate({'x': x}))
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
            if(f[len(f)-1] >= f[len(f)-2]) and (ok == True):
                break
    return (y[len(y)-2])

#Metodo Secao Aurea
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
    return (x,k)

#Metodo Busca Fibonacci
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
    return (x, k)

#Metodo Metodo Newton
def MetodoNewton(funcao, a, b, epsilon):
    x, y, z = symbols('x y z')
    init_printing(use_unicode=True)

    x = a
    deriv1 = str(diff(funcao))
    d1 = float(parser.parse(deriv1).evaluate({'x' : x}))    
    k = []
    k.append(x)

    while abs(float(d1)) >= epsilon:
        
        deriv2 = str(diff(deriv1))
        d2 = float(parser.parse(deriv2).evaluate({'x' : x}))
        
        if d2 != 0.0:
            x = k[len(k)-1] - (d1 / d2)
            k.append(x)
            if((abs(k[len(k)-1] - k[len(k)-2]) / max(1, abs(k[len(k)-2]))) < epsilon):         
                break
            else:
                d1 = float(parser.parse(deriv1).evaluate({'x' : x}))
        else:
            break
    return (k[len(k)-1])

window1, window2, window3, window4, window5, window6, window7 = main_window(), None, None, None, None, None, None
parser = Parser()

while True:
    window, event, valores = sg.read_all_windows()
    if event == 'Sair'or event == sg.WIN_CLOSED:
        window.close()

    if window== window1 and event == 'Busca Uniforme':
        window2 = window_buscaUniforme()
        window2.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Busca Dicotômica':
        window3 = window_buscaDicotomica()
        window3.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Seção Áurea':
        window4 = window_secaoAurea()
        window4.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Busca Fibonacci':
        window5 = window_buscaFibonacci()
        window5.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window== window1 and event == 'Bisseção':
        window6 = window_bissecao()
        window6.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)
        
    if window== window1 and event == 'Newton':
        window7 = window_newton()
        window7.move(window1.current_location()[0] + 50, window1.current_location()[1] + 50)

    if window == window2 and event == 'Calcular':
        x = float(valores['valor_a'])
        atualizarResultado = str(parser.parse(valores['expressao']).evaluate({'x': x}))
        resultado = BuscaUniforme(float(valores['valor_a']),float(valores['valor_b']), float(valores['delta']), atualizarResultado, valores['expressao'])
        window2['respostaUniforme1'].update('RESULTADO: ')
        window2['respostaUniforme2'].update('x* = %.4f' % resultado)
    
    if window == window4 and event == 'Calcular':
        resultado = SecaoAurea(float(valores['valor_a']),float(valores['valor_b']),float(valores['epsilon']))
        window4['respostaAurea1'].update('RESULTADO: ')
        window4['respostaAurea2'].update('x* = %.4f' % resultado[0])
        window4['respostaAurea3'].update('K variando de 1 a %d' % resultado[1])

    if window == window5 and event == 'Calcular':
        resultado = Fibonacci(float(valores['valor_a']),float(valores['valor_b']),float(valores['epsilon']))
        window5['respostaFibonacci1'].update('RESULTADO: ')
        window5['respostaFibonacci2'].update('x* = %.4f' % resultado[0])
        window5['respostaFibonacci3'].update('K variando de 1 a %d' % resultado[1])
    
    if window == window7 and event == 'Calcular':
        funcao = str(parser.parse(valores['expressao']))
        resultado = MetodoNewton(funcao,float(valores['valor_a']),float(valores['valor_a']),float(valores['epsilon']))
        window7['respostaNewton1'].update('RESULTADO: ')
        window7['respostaNewton2'].update('x* = %.4f' % resultado)
