from django.shortcuts import render

# Create your views here.
from textwrap import wrap
import math

#32 BITS
def decimalABinario32(numero):
    binario=format(numero, "b")
    return binario

def decimalABinarioFrac32(numero):
    binario=""
    while len(binario) <= 32:
        numero = numero * 2
        resi, entero = math.modf(numero)
        numero=numero-int(entero)
        binario=binario+str(int(entero))
    return binario

def completacion32(binario):
    tamano = len(binario)
    restante = tamano - 23
    restante = abs(restante)
    cero = "0"
    if(restante != 0):
        binario = binario + cero * restante
        return binario
    else:
        return binario

def exponente_exceso32(binosaurio):
    possicion = str(binosaurio).find('.') -1
    n = possicion -1
    exponente = possicion + 127
    return exponente

def normalisacion32(binosaurio):
    numero = binosaurio.replace(".", "")
    numero = numero[:1] + "." + numero[1:]
    return numero[:25]

#64 BITS
def decimalABinario(numero):
    binario = format(numero, "b")
    return binario

def decimalABinarioFrac(numero):
    binario = ""
    while len(binario) <= 64:
        numero = numero * 2
        resi, entero = math.modf(numero)
        numero = numero - int(entero)
        binario = binario + str(int(entero))
    return binario

def completacion(binario):
    tamano = len(binario)
    restante = tamano - 52
    restante = abs(restante)
    cero = "0"
    if (restante != 0):
        binario = binario + cero * restante
        return binario
    else:
        return binario

def exponente_exceso(binosaurio):
    possicion = str(binosaurio).find('.') - 1
    n = possicion - 1
    exponente = possicion + 1023
    return exponente

def normalisacion(binosaurio):
    numero = binosaurio.replace(".", "")
    numero = numero[:1] + "." + numero[1:]
    return numero[:25]

def vista64(request):
    numero = request.POST['64bits']
    if (str(numero).find(".") == -1):
        numeroConvertidoBinario = decimalABinario(int(numero))
    else:
        residuo, entero = math.modf(float(numero))
        entero = int(entero)
        numeroConvertidoBinario = decimalABinario(
            entero) + "." + decimalABinarioFrac(residuo)

    binario=numeroConvertidoBinario
    print("binario: " + numeroConvertidoBinario)
    normal = normalisacion(numeroConvertidoBinario)

    normalReal= normal
    print("normalisacion: " + normal)
    normal = completacion(normal)
    if (float(numero) > 0):
        print("signo: 0")
        signo=" 0"
    else:
        print("signo: 1")
        signo=" 1"
    l_partes = str(normal).split('.')

    mantisa= l_partes[1]
    print("mantisa: " + l_partes[1])
    sexponente_decimal = exponente_exceso(numeroConvertidoBinario)

    expDecimal=str(sexponente_decimal)
    print("exponente decimal:" + str(sexponente_decimal))

    expBin= decimalABinario(sexponente_decimal)
    print("exponente binario:" + decimalABinario(sexponente_decimal))

    return render(request, '64Bits.html',
                  {'numero': numero,'binario': binario, 'normal': normalReal, 'signo': signo,
                   'mantisa': mantisa, 'expDecimal': expDecimal, 'expBin': expBin})



#PARA 32 BITS



def completacion2(binario):
    tamano = len(binario)
    restante = tamano - 23
    restante = abs(restante)
    cero = "0"
    if(restante != 0):
        binario = binario + cero * restante
        return binario
    else:
        return binario

def exponente_exceso2(binosaurio):
    possicion = str(binosaurio).find('.') -1
    n = possicion -1
    exponente = possicion + 127
    return exponente


def normalisacion2(binosaurio):
    numero = binosaurio.replace(".", "")
    numero = numero[:1] + "." + numero[1:]
    return numero[:25]


def vista32(request):
    numero = request.POST['32bits']
    if(str(numero).find(".") == -1):
        numeroConvertidoBinario = decimalABinario32(int(numero))
    else:
        residuo, entero = math.modf(float(numero))
        entero = int(entero)
        numeroConvertidoBinario = decimalABinario32(entero)+"."+decimalABinarioFrac32(residuo)

    binario = numeroConvertidoBinario
    print("binario: " + numeroConvertidoBinario)
    normal = normalisacion2(numeroConvertidoBinario)

    normalReal = normal
    print("normalisacion: " + normal)
    normal = completacion2(normal)
    if(float(numero) > 0):
        print("signo: 0" )
        signo = " 0"
    else:
        print("signo: 1")
        signo = " 1"
    l_partes = str(normal).split('.')

    mantisa = l_partes[1]
    print("mantisa: " + l_partes[1])
    sexponente_decimal = exponente_exceso2(numeroConvertidoBinario)

    expDecimal = str(sexponente_decimal)
    print("exponente decimal:" + str(sexponente_decimal))

    expBin = decimalABinario(sexponente_decimal)
    print("exponente binario:" + decimalABinario(sexponente_decimal))

    return render(request, '32Bits.html',
                  {'numero': numero, 'binario': binario, 'normal': normalReal, 'signo': signo,
                   'mantisa': mantisa, 'expDecimal': expDecimal, 'expBin': expBin})




def vista32Bits(request):
    return render(request,"32Bits.html")

def vista64Bits(request):
    return render(request,"64Bits.html")

