# -*- coding:utf-8 -*- 
import math 
 
def sumar():# Funcion para suma 
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el Segundo numero: "))
    return 'El resultado de {} + {} es: {}\n'.format(a,b,a+b)
def restar(): 
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el Segundo numero: "))
    return 'El resultado de {} - {} es: {}\n'.format(a,b,a-b)
def multiplicar(): 
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el Segundo numero: "))
    return 'El resultado de {} x {} es: {}\n'.format(a,b,a*b)
def dividir(): 
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el Segundo numero: "))
    return 'El resultado de {} / {} es: {}\n'.format(a,b,a/b)
def potenciar(): 
    a = float(input("Ingrese el numero base: "))
    b = float(input("Ingrese la potencia: "))
    return 'El resultado de {} ^ {} es: {}\n'.format(a,b,a**b)
def OperarLogaritmo(): 
    a = float(input("Ingrese el numero: "))
    return 'El resultado de logaritmo natural es: {}\n'.format(math.log(a))
def OperarRaiz(): 
    a = float(input("Ingrese el radicando: "))
    b = float(input("Ingrese el indice de la raíz: ")) 
    return 'El resultado de ((raíz de {})^{}) es: {}\n'.format(a,b,pow(a,1/b))
def OperarSeno(): 
    a = float(input("Ingrese el numero: ")) 
    return 'El resultado de (seno de {}) es: {}\n'.format(a,math.sin(a))
def OperarCoseno(): 
    a = float(input("Ingrese el numero: ")) 
    return 'El resultado de (coseno de {}) es: {}\n'.format(a,math.cos(a))
def OperarModulo(): 
    a = float(input("Ingrese el numero: ")) 
    b = float(input("Ingrese el segúndo números: "))
    return 'El resultado del (Módulo de esta operación es: {}\n'.format(a%b)
def menu(): 
    operacion = input(""" 
    \t-> (+) Para sumar 
    \t-> (-) Para restar 
    \t-> (*) Para Multiplicar 
    \t-> (/) Para dividir 
    \t-> (**)Para elevar a un exponente 
    \t-> (Ln) Para logaritmo natural 
    \t-> (sqrd) Para raíz 
    \t-> (S) Para seno 
    \t-> (C) Para coseno 
    \t-> (%) Módulo
    \t----> \t"""); 
    if operacion == "+": 
        resultado = sumar(); 
    elif operacion == "-": 
        resultado = restar(); 
    elif operacion == "*": 
        resultado = multiplicar(); 
    elif operacion == "/": 
        resultado = dividir(); 
    elif operacion == "**": 
        resultado = potenciar(); 
    elif operacion == "Ln" or operacion == "ln": 
        resultado = OperarLogaritmo(); 
    elif operacion == "sqrd" or operacion == "sqrd": 
        resultado = OperarRaiz(); 
    elif operacion == "S" or operacion == "s": 
        resultado = OperarSeno(); 
    elif operacion == "C" or operacion == "c": 
        resultado = OperarCoseno(); 
    elif operacion == "%": 
        resultado = OperarModulo(); 
    else: 
        resultado = "No se encontro la operarción que indicó.\n" 
    return resultado; 
salir = ""; 
while  salir.lower() != "no": 
    print(menu()) 
    salir = input("(Si) para volver a usar la calculadora\n(no) para salir\n---> ");