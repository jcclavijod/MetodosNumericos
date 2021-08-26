
from django.shortcuts import render, redirect
from textwrap import wrap
import math
#Ecuaciones no lineales
import sympy
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from sympy import exp, E, log






def vistaIndex(request):
    return render(request,"index.html")

def vistaBinaria(request):
    return render(request,"baseBinaria.html")

def vistaOctal(request):
    return render(request,"baseOctal.html")

def vistaDecimal(request):
    return render(request,"baseDecimal.html")

def vistaHexadecimal(request):
    return render(request,"baseHexadecimal.html")

#CALCULOS BASE DECIMAL

def decimalABinario(numero):
    binario=format(numero, "b")
    return binario

def decimalABinarioFrac(numero):
    binario=""
    while len(binario) <= 12:
        numero = numero * 2
        resi, entero = math.modf(numero)
        numero=numero-int(entero)
        binario=binario+str(int(entero))
    return binario

def decToOctal(n):
    l_partes = str(n).split('.')
    n = int(l_partes[0])
    octalNum = [0] * 100
    i = 0
    octal=""
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        octal+=str(octalNum[j])
    return octal

def decimalww(decimal):
    l_partes = str(decimal).split('.')
    decimal=l_partes[1]
    uwu = "0."+decimal
    numero = float(uwu)
    array = []
    for x in range(12):
        numero = numero *8
        l_partes = str(numero).split('.')
        array.append(l_partes[0])
        numero = "0."+l_partes[1]
        numero = float(numero)
    x = "".join(str(e)for e in array)
    return x


def decToHexaInt(numero):
    hexa = hex(numero)
    hexa=hexa.upper()[2:]
    return hexa


def decToHexaFloat(numero):
    residuo2, entero2 = math.modf(float(numero))
    hexa2 = residuo2
    auxiliar = decToHexaInt(int(entero2))
    hexaDecimal=""
    while len(hexaDecimal) <= 7:
        hexa2 = hexa2 * 16
        resi, entero = math.modf(hexa2)
        hexa2=hexa2-int(entero)
        hexaDecimal += decToHexaInt(int(entero))
    conversion=auxiliar + "."+hexaDecimal
    return conversion

#CALCULOS BASE OCTAL

def OctaDecimal(numero):
    sistema = int(8)
    numoctadec = int(str(numero), sistema)
    return numoctadec

def OctalAdecimalfloat(numero):
    valor = 0
    for idx in range(len(numero)):
        if numero[idx] == '.':
            break
        value = int(numero[idx], 8)
        valor = valor * 8 + value

    fraccion = 1 / 8
    for idx in range(idx + 1, len(numero)):
        value = int(numero[idx], 8)
        valor = valor + value * fraccion
        fraccion /= 8
    return valor

#BINARIO A DECIMAL

def BinaDecimal(numero):
    numero=str(int(numero))
    decimal=int(numero,2)
    return decimal

def binarioADecimalFrac(numero):
    l_partes = numero.split('.')
    num_frac = l_partes[1]
    soma = 0.0
    for cont in range(len(num_frac)):
        num_dig = float(num_frac[cont])
        exp = -(cont + 1)
        soma += num_dig * 2 ** exp
    return soma

#CALCULOS BASE HEXADECIMAL

def HexaDecimalINT(numero):
    sistema = int(16)
    numint = int(str(numero), sistema)
    return numint #retorna el total

def HexaAdecimal(numero):
    valor = 0
    for idx in range(len(numero)):
        if numero[idx] == '.':
            break
        value = int(numero[idx], 16)
        valor = valor * 16 + value

    fraccion = 1 / 16
    for idx in range(idx + 1, len(numero)):
        value = int(numero[idx], 16)
        valor = valor + value * fraccion
        fraccion /= 16
    return valor

#CONVERSIONES COMPLETA

def vistaResultadoBinario(request):
    numero = request.POST['binario']
    if "." in str(numero):
        residuo, entero = math.modf(float(numero))
        l_partes = numero.split('.')
        numeroConvertidoDecimal = BinaDecimal(l_partes[0]) + binarioADecimalFrac(numero)
        numeroConvertidoOctal = decToOctal(numeroConvertidoDecimal) + "." + decimalww(numeroConvertidoDecimal)
        numeroConvertidoHexa = decToHexaFloat(numeroConvertidoDecimal)
    else:
        numeroConvertidoDecimal = BinaDecimal(numero)
        numeroConvertidoOctal = decToOctal(numeroConvertidoDecimal)
        numeroConvertidoHexa = decToHexaInt(int(numeroConvertidoDecimal))

    return render(request, 'resultadosConv/resultadoBinario.html', {'numero': numero,'decimal': numeroConvertidoDecimal,
                                               'octal': numeroConvertidoOctal, 'hexadecimal': numeroConvertidoHexa})

def vistaResultadoOctal(request):
    numero = request.POST['octal']
    if "." in str(numero):
        numeroConvertidoDecimal = OctalAdecimalfloat(numero)
        residuo, entero = math.modf(float(numeroConvertidoDecimal))
        entero = int(entero)
        numeroConvertidoBinario = decimalABinario(entero) + "." + decimalABinarioFrac(residuo)
        numeroConvertidoHexa = decToHexaFloat(numeroConvertidoDecimal)
    else:
        numeroConvertidoDecimal = OctaDecimal(numero)
        numeroConvertidoBinario = decimalABinario(int(numeroConvertidoDecimal))
        numeroConvertidoHexa = decToHexaInt(int(numeroConvertidoDecimal))

    return render(request, 'resultadosConv/resultadoOctal.html', {'numero': numero,'decimal': numeroConvertidoDecimal,
                                               'binario': numeroConvertidoBinario, 'hexadecimal': numeroConvertidoHexa})

def vistaResultadoHexadecimal(request):
    numero = request.POST['hexadecimal']
    if "." in str(numero):
        numeroConvertidoDecimal = HexaAdecimal(numero)
        residuo, entero = math.modf(float(numeroConvertidoDecimal))
        entero = int(entero)
        numeroConvertidoBinario = decimalABinario(entero) + "." + decimalABinarioFrac(residuo)
        numeroConvertidoOctal = decToOctal(numeroConvertidoDecimal) + "." + decimalww(numeroConvertidoDecimal)
    else:
        numeroConvertidoDecimal = HexaDecimalINT(numero)
        numeroConvertidoBinario = decimalABinario(int(numeroConvertidoDecimal))
        numeroConvertidoOctal = decToOctal(numeroConvertidoDecimal)

    return render(request, 'resultadosConv/resultadoHexadecimal.html', {'numero': numero,'decimal': numeroConvertidoDecimal,
                                               'binario': numeroConvertidoBinario, 'octal': numeroConvertidoOctal})

def vistaResultadoDecimal(request):
    numero= request.POST['decimal']
    if "." in str(numero):
        numeroConvertidoOctal = decToOctal(numero) + "." + decimalww(numero)
        residuo, entero = math.modf(float(numero))
        entero = int(entero)
        numeroConvertidoBinario = decimalABinario(entero) + "." + decimalABinarioFrac(residuo)
        numeroConvertidoHexa = decToHexaFloat(numero)
    else:
        numeroConvertidoOctal = decToOctal(numero)
        numeroConvertidoBinario = decimalABinario(int(numero))
        numeroConvertidoHexa = decToHexaInt(int(numero))

    return render(request, 'resultadosConv/resultadoDecimal.html', {'numero': numero,'octal': numeroConvertidoOctal,'binario': numeroConvertidoBinario,
                                               'hexadecimal': numeroConvertidoHexa})

def vistaDerivadas(request):
    return render(request,"derivadas.html")



# ---------------------------------ECUACIONES NO LINEALES------------------------------------------

def vistaSolucion(request):
    x = symbols('x')  # Declarar variable independiente
    fun_escrita = request.POST['funcion']
    evaluador=float(request.POST['evaluar'])
    f = parse_expr(fun_escrita)
    funcionEval=sympy.sympify(f).subs(x, evaluador)
    dact = diff(f, x)
    derivada = str(simplify(dact))
    evaluada = sympy.sympify(derivada).subs(x, evaluador)

    dact2 = diff(f, x, 2)
    derivada2 = str(simplify(dact2))
    evaluada2 = sympy.sympify(derivada2).subs(x,evaluador)

    return render(request, 'derivadas.html',
                  {'f': funcionEval,'derivada': derivada, 'derivada2': derivada2,
                   'evaluada': evaluada, 'evaluada2': evaluada2})

def secanteSolucion(request):
    f = request.POST['funcion']
    x0 = float(request.POST['x0'])
    x1 = float(request.POST['x1'])
    eMax = float(request.POST['eMax'])
    N = 100
    lista=[]
    funcs = vars(math)
    for k in range(N):
        if x1 - x0 == 0:
            break
        fp = (eval(f, funcs, dict(x=x1)) - eval(f, funcs, dict(x=x0))) / (x1 - x0)
        x = x1 - eval(f, funcs, dict(x=x1)) / fp
        e = abs((x - x1) / x)
        if e < eMax:
            break
        x0 = x1
        x1 = x
        fx=eval(f, funcs, dict(x=x))
        lista.append([str(k+1),str(x),str(fx),str(e)])
        em=e
        xtot=x
        print(k + 1, x, eval(f, funcs, dict(x=x)), e)
    return render(request, 'resultadoSecante/secante.html',
                  {'raiz': xtot, 'error': str(em),
                   'fx': str(fx),'lista':lista})

def vistaSecante(request):
    return render(request,"secante.html")


def vistaDecimal32(request):
    return render(request, "decimalABit32.html")

def vistaDecimalBit32(request):
    S = request.POST['signo']
    E = request.POST['exponente']
    M = request.POST['mantisa']
    N= S + E + M
    a = int(N[0])        # sign,     1 bit
    b = int(N[1:9],2)    # exponent, 8 bits
    c = int("1"+N[9:], 2)# fraction, len(N)-9 bits
    salida=(-1)**a * c /( 1<<( len(N)-9 - (b-127) ))
    return render(request, 'decimalABit32.html',
                  {'salida': salida,'signo': S,'exponente': E,'mantisa': M})


def vistaDecimal64(request):
    return render(request, "decimalABit64.html")

def vistaDecimalBit64(request):
    S = request.POST['signo']
    E = request.POST['exponente']
    M = request.POST['mantisa']
    N = S + E + M
    a = int(N[0])  # sign, 1 bit
    b = int(N[1:12], 2)  # exponent, 12 bits
    c = int("1" + N[12:], 2)  # fraction,
    salida = (-1)**a * c /( 1<<( len(N)-12 - (b-1023) ))
    return render(request, 'decimalABit64.html',
                  {'salida': salida,'signo': S,'exponente': E,'mantisa': M})

def vistaGraficar(request):
    return render(request, "graficas.html")


def f(expr,value):
    x = var('x')
    res = expr.subs(x, value)
    return res

def derivada(expr,value):
    x = Symbol('x')
    deriva = diff(expr, x)
    return deriva.subs(x, value)

def newton(expr,x_old):
    x = var('x')
    x_new = x_old - f(expr,x_old)/derivada(expr,x_old)
    return x_new

def vistaNewton(request):
    x = var('x')
    user_input = request.POST['funcion']
    expr = sympify(user_input)
    x_old = float(request.POST['x0'])
    RAE = float(request.POST['error'])
    RAE_now = 100
    counter = 0
    lista=[]
    while RAE < RAE_now:
        x_new = newton(expr,x_old)
        selisih = abs(x_new-x_old)
        RAE_now = abs(selisih/x_new)
        x_old = x_new
        counter = counter+1
        print(counter, x_new, RAE_now)
        lista.append([counter, x_new, RAE_now])
    return render(request, 'resultadoSecante/newtonSolucion.html',
                  {'raiz': x_new, 'error': RAE_now,
                   'lista': lista})

def vistaNew(request):
    return render(request, "newton.html")