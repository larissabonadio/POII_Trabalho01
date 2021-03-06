import PySimpleGUI as sg
from sympy.polys.polyoptions import Symbols
from py_expression_eval import Expression, Parser
from sympy import *
from decimal import Decimal
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
            [sg.Text(size=(40,1), key='respostaUniforme2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaUniforme3', text_color = 'black')]
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
            [sg.Text(size=(40,1), key='respostaDicotomica2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaDicotomica3', text_color = 'black')]
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
            [sg.Text(size=(40,1), key='respostaBissecao2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaBissecao3', text_color = 'black')]
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
            [sg.Text(size=(40,1), key='respostaNewton2', text_color = 'black')],
            [sg.Text(size=(40,1), key='respostaNewton3', text_color = 'black')]
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

def BuscaUniforme(a, b, delta, atualizarResultado, funcao):
    f = []     
    y = []    
    x = a
    ok = False
    k = 0
    while x <= b:
        y.append(x)
        atualizarResultado = str(parser.parse(valores['expressao']).evaluate({'x': x}))
        f.append(float(atualizarResultado))

        if len(y) > 1 and len(f) > 1:    
            if(f[len(f)-1] > f[len(f)-2]) and (ok == False):
                ok = True
                y.pop()
                y.pop()
                f.pop()
                f.pop()
                delta = delta / 10
                if len(y) == 0:
                    return (a, 0)
                else:
                    x = y[len(y)-1]  
            if(f[len(f)-1] >= f[len(f)-2]) and (ok == True):
                break
        x = x + delta
        k = k + 1
        if (k==10000):
            return (y[len(y)-2], -1)
    return (y[len(y)-2], k)

def BuscaDicotomica(a, b, delta, epsilon, funcao):
    k=1
    while (b-a)>=epsilon:
        x = ((a+b)/2)-delta
        z = ((a+b)/2)+delta
        fx = float(parser.parse(valores['expressao']).evaluate({'x': x}))
        fz = float(parser.parse(valores['expressao']).evaluate({'x': z}))
        if fx>fz:
            a = x
        elif fx<=fz:
            b = z
        k = k+1
        if (k==10000):
            return ((a+b)/2, 0)
    x = (a+b)/2
    return (x, k)
    
def SecaoAurea(a, b, epsilon):
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
        if (k==10000):
            return ((a+b)/2, 0)
    x = (a+b)/2
    k += 1
    return (x,k)

def Fibonacci(a, b, epsilon):
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

def MetodoBissecao (funcao, a, b, epsilon):
    iteracoes = (math.log((b-a)/epsilon)/math.log(2))*1.0
    iteracoes = int(round(iteracoes+0.5))
    k=1
    d=1
    for i in range (0, iteracoes):
        x = (a+b)/2
        deriv = str(diff(funcao))
        d = float(parser.parse(deriv).evaluate({'x' : x}))
        if d==0:
            return (x, k)
        elif d>0:
            b = x
        else:
            a = x
        if k!=iteracoes:
            k = k+1
    return ((a+b)/2, k)

def MetodoNewton(funcao, a, b, epsilon):
    x, y, z = symbols('x y z')
    init_printing(use_unicode=True)

    x = a
    deriv1 = str(diff(funcao))
    d1 = float(parser.parse(deriv1).evaluate({'x' : x}))    
    k = []
    k.append(x)
    l = 0
    
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
        l = l + 1
    return (k[len(k)-1], l)

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
        window2['respostaUniforme2'].update('x* = %.4f' % resultado[0])
        if resultado[1] == 0:
            window2['respostaUniforme3'].update('Não foi possível realizar o refinamento')
        elif resultado[1]==-1:
            window2['respostaUniforme3'].update('K variando de 1 a 10000: O método não converge')
        else:
            window2['respostaUniforme3'].update('K variando de 1 a %d' % resultado[1])
    
    if window == window3 and event == 'Calcular':
        resultado = BuscaDicotomica(float(valores['valor_a']), float(valores['valor_b']), float(valores['delta']), float(valores['epsilon']), valores['expressao'])
        window3['respostaDicotomica1'].update('RESULTADO: ')
        window3['respostaDicotomica2'].update('x* = %.4f' % resultado[0])
        if resultado[1] == 0:
            window3['respostaDicotomica3'].update('K variando de 1 a 10000: O método não converge')
        else:
            window3['respostaDicotomica3'].update('K variando de 1 a %d' % resultado[1])

    if window == window4 and event == 'Calcular':
        resultado = SecaoAurea(float(valores['valor_a']),float(valores['valor_b']),float(valores['epsilon']))
        window4['respostaAurea1'].update('RESULTADO: ')
        window4['respostaAurea2'].update('x* = %.4f' % resultado[0])
        if resultado[1] == 0:
            window4['respostaAurea3'].update('K variando de 1 a 10000: O método não converge')
        else:
            window4['respostaAurea3'].update('K variando de 1 a %d' % resultado[1])

    if window == window5 and event == 'Calcular':
        resultado = Fibonacci(float(valores['valor_a']),float(valores['valor_b']),float(valores['epsilon']))
        window5['respostaFibonacci1'].update('RESULTADO: ')
        window5['respostaFibonacci2'].update('x* = %.4f' % resultado[0])
        window5['respostaFibonacci3'].update('K variando de 0 a %d' % resultado[1])
    
    if window == window6 and event == 'Calcular':
        resultado = MetodoBissecao(valores['expressao'], float(valores['valor_a']),float(valores['valor_b']),float(valores['epsilon']))
        window6['respostaBissecao1'].update('RESULTADO: ')
        window6['respostaBissecao2'].update('x* = %.4f' % resultado[0])
        window6['respostaBissecao3'].update('K variando de 1 a %d' % resultado[1])

    if window == window7 and event == 'Calcular':
        funcao = str(parser.parse(valores['expressao']))
        resultado = MetodoNewton(funcao,float(valores['valor_a']),float(valores['valor_a']),float(valores['epsilon']))
        window7['respostaNewton1'].update('RESULTADO: ')
        window7['respostaNewton2'].update('x* = %.4f' % resultado[0])
        window7['respostaNewton3'].update('K variando de 1 a %d' % resultado[1])
