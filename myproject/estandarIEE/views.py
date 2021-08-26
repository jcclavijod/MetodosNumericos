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
        numeroConvertidoBinario2 = decimalABinario(int(numero))
    else:
        residuo2, entero2 = math.modf(float(numero))
        entero = int(entero2)
        numeroConvertidoBinario2 = decimalABinario(
            entero) + "." + decimalABinarioFrac(residuo2)

    binario2=numeroConvertidoBinario2
    print("binario: " + numeroConvertidoBinario2)
    normal2 = normalisacion(numeroConvertidoBinario2)

    normalReal2= normal2
    print("normalisacion: " + normal2)
    normal2 = completacion(normal2)
    if (float(numero) > 0):
        print("signo: 0")
        signo2=" 0"
    else:
        print("signo: 1")
        signo2=" 1"
    l_partes2 = str(normal2).split('.')

    mantisa2= l_partes2[1]
    print("mantisa: " + l_partes2[1])
    sexponente_decimal2 = exponente_exceso(numeroConvertidoBinario2)

    expDecimal2=str(sexponente_decimal2)
    print("exponente decimal:" + str(sexponente_decimal2))

    expBin2= decimalABinario(sexponente_decimal2)
    print("exponente binario:" + decimalABinario(sexponente_decimal2))

    return render(request, '64Bits.html',
                  {'numero': numero,'binario2': binario2, 'normal2': normalReal2, 'signo2': signo2,
                   'mantisa2': mantisa2, 'expDecimal2': expDecimal2, 'expBin2': expBin2})



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
    normal = normalisacion2(numeroConvertidoBinario)
    normalReal = normal
    normal = completacion2(normal)
    if(float(numero) > 0):
        signo = " 0"
    else:
        signo = " 1"
    l_partes = str(normal).split('.')
    mantisa = l_partes[1]
    sexponente_decimal = exponente_exceso2(numeroConvertidoBinario)
    expDecimal = str(sexponente_decimal)
    expBin = decimalABinario(sexponente_decimal)

    #64
    if (str(numero).find(".") == -1):
        numeroConvertidoBinario2 = decimalABinario(int(numero))
    else:
        residuo2, entero2 = math.modf(float(numero))
        entero = int(entero2)
        numeroConvertidoBinario2 = decimalABinario(
            entero) + "." + decimalABinarioFrac(residuo2)
    binario2=numeroConvertidoBinario2
    normal2 = normalisacion(numeroConvertidoBinario2)
    normalReal2= normal2
    normal2 = completacion(normal2)
    if (float(numero) > 0):
        signo2=" 0"
    else:
        signo2=" 1"
    l_partes2 = str(normal2).split('.')
    mantisa2= l_partes2[1]
    sexponente_decimal2 = exponente_exceso(numeroConvertidoBinario2)
    expDecimal2=str(sexponente_decimal2)
    expBin2= decimalABinario(sexponente_decimal2)

    return render(request, 'resultadoBits/ambosBits.html',
                  {'numero': numero, 'binario': binario, 'normal': normalReal, 'signo': signo,
                   'mantisa': mantisa, 'expDecimal': expDecimal, 'expBin': expBin,'binario2': binario2, 'normal2': normalReal2, 'signo2': signo2,
                   'mantisa2': mantisa2, 'expDecimal2': expDecimal2, 'expBin2': expBin2})




def vista32Bits(request):
    return render(request,"32Bits.html")

def vista64Bits(request):
    return render(request,"64Bits.html")

