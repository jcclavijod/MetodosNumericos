
from django.shortcuts import render, redirect
from textwrap import wrap
import math
#Ecuaciones no lineales
import sympy
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

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

    dact = diff(f, x)
    derivada = str(simplify(dact))
    evaluada = sympy.sympify(derivada).subs(x, evaluador)

    dact2 = diff(f, x, 2)
    derivada2 = str(simplify(dact2))
    evaluada2 = sympy.sympify(derivada2).subs(x,evaluador)

    return render(request, 'derivadas.html',
                  {'derivada': derivada, 'derivada2': derivada2,
                   'evaluada': evaluada, 'evaluada2': evaluada2})
