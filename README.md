# POII - Trabalho01: Programação Não Linear Monovariável #

O trabalho apresenta o desenvolvimento de um programa que determina o ponto de mínimo de uma função, sendo resolvida por um dos métodos abaixo:
    
    1. Busca Uniforme
    
    2. Busca Dicotômica 
    
    3. Seção Áurea 
    
    4. Busca de Fibonacci 
    
    5. Método da Bisseção
    
    6. Método de Newton
    
 O usuário poderá escolher entre os métodos acima, e a partir da sua escolha inserir as informações de entrada necessárias para obter a solução, juntamente com a quantidade de iterações feita pelo método.
 
Inicialmente seu ambiente foi preparado para receber apenas expressões matemáticas monovariáveis, além disso seus métodos foram escrito da forma análoga ao apresentado na realidade. 

Neste trabalho foi utilizado o avaliador de expressão matemática py_expression_eval, na linguagem de programação Python, de modo.

Abaixo serão descrito alguns aspectos e restrições para o uso adequado do avaliador py_expression_eval.

Operadores:

    + : Soma

    - : Subtração

    * : Multiplicação

    / : Divisão

    ^ : Potência
    
    % : Divisão inteira

    sqrt(x): Raiz Quadrada

Constantes:

    E = 2.718281828459045 (Constante de Euler)

    PI = 3,141592653589793 (PI) 

Funções Trigonométricas:

    sin(x)	: Seno

    cos(x)	: Cosseno

    tan(x)	: Tangente

    asin(x) : Arco seno

    acos(x) : Arco cosseno 

    atan(x) : Arco tangente


Outras Funções:

    log(x)	: Logaritmo com base 10

    log(x, base) : Logaritmo com base da escolha do usuário

    abs(x)	: Valor absoluto

    ceil(x) : Teto de x (o menor inteiro que é >= x)

    floor(x) : Piso de x (o maior inteiro que é <= x)

    round(x) : Arredondado para o número inteiro mais próximo

    exp(x) : Exponencial

Segue alguns exemplos de como utilizar o programa:

    Valor decimal (utiliza-se .): 0.5

    Escrita da função: 
                    
                     x^2-3*x+2

                     E^x+2

                     x*sin(PI*x)

                     sqrt(16)

                     log(2.7)

                     log(E)
