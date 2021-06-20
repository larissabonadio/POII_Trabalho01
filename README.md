# POII - Trabalho01: Programação Não Linear Monovariável #

#### Grupo: ####
Giulia Rossatto Rocha - RA: 191025372
Larissa de Castro Bonadio - RA: 191020222
Larissa Mayumi Barela Hondo - RA: 191026123


Trabalho realizado em Python 3.

O trabalho apresenta o desenvolvimento de um programa que determina o ponto de mínimo de uma função, sendo resolvida por um dos métodos abaixo:
    
    1. Busca Uniforme
    
    2. Busca Dicotômica 
    
    3. Seção Áurea 
    
    4. Busca de Fibonacci 
    
    5. Método da Bisseção
    
    6. Método de Newton
    
 O usuário poderá escolher entre os métodos acima, e a partir da sua escolha inserir as informações de entrada necessárias para obter a solução, juntamente com a quantidade de iterações feita pelo método.
 
Inicialmente seu ambiente foi preparado para receber apenas expressões matemáticas monovariáveis, além disso seus métodos foram escrito da forma análoga ao apresentado na realidade. 

Neste trabalho foi utilizado o avaliador de expressão matemática py_expression_eval, na linguagem de programação Python. Abaixo serão descrito alguns aspectos e restrições para o uso adequado do avaliador.

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

### OBSERVAÇÕES IMPORTANTES: ###

Para multiplicação é OBRIGATÓRIO o uso do multiplicador *:

    ERRADO: 2x

    CERTO: 2*x

    
Para utilizações das funções acima, é necessário utilizar a mesma escrita para o interpretador reconhecer:

    ERRADO: seno(x), sen(x)

    CERTO: sin(x)

É NECESSÁRIO UTILIZAR A VARIÁVEL INDEPENDENTE X PARA AS FUNÇÕES! Outras variáveis como a, b, c, x1, z, etc não serão reconhecidas pelo interpretador.

    ERRADO: 2*a+2

    CERTO: 2*x+2

NÃO UTILIZAR VÍRGULA PARA REPRESENTAR DECIMAIS

    ERRADO: 0,01
    
    CERTO: 0.01

NÃO UTILIZAR BASE 10 PARA INSERIR VALORES DE DELTA (Δ) E EPSILON (ε):

    ERRADO: 10^(-2)
    
    CERTO: 0.01


EXEMPLO PARA MÉTODO DE BUSCA DICOTÔMICA:

    Inserir função: x^2-3*x+2
    a = 0.5
    b = 2.5
    Δ = 0.01
    ε = 0.1

O resultado a ser gerado será: 

    x* = 1.5309
    K variando de 1 a 6
