import random
import re as standardre
import numpy as np
from django.shortcuts import render, redirect
import math
import sympy
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy import *
from sympy import exp, E, log
from .forms import numberForm
import fractions

np.set_printoptions(formatter={'all': lambda x: str(fractions.Fraction(x).limit_denominator())})

dicMatrices = dict()
agregadas = []
datos = dict()
result = []
resulado = []
resultado_a_c = []
fil = 0
col = 0

mt1 = [[1, 2, 3], [3, 4, 5]]
mt21 = np.array(mt1).reshape(3, 2)
dicMatrices.update({"matri1": mt21})

mt2 = [[3, 22, 12.3], [30, 1, 33]]
mt22 = np.array(mt2).reshape(3, 2)
dicMatrices.update({"matri2": mt22})

copiaMostrar = dict()
copiaMostrar.update({"matri1": mt21})
copiaMostrar.update({"matri2": mt22})

agregadas = []
agregadas.append([mt21, 3, 2])
agregadas.append([mt22, 3, 2])

listaM = dict()


def vistaIndex(request):
    return render(request, "index.html")


def vistaBinaria(request):
    return render(request, "baseBinaria.html")


def vistaOctal(request):
    return render(request, "baseOctal.html")


def vistaDecimal(request):
    return render(request, "baseDecimal.html")


def vistaHexadecimal(request):
    return render(request, "baseHexadecimal.html")


# CALCULOS BASE DECIMAL

def decimalABinario(numero):
    binario = format(numero, "b")
    return binario


def decimalABinarioFrac(numero):
    binario = ""
    while len(binario) <= 12:
        numero = numero * 2
        resi, entero = math.modf(numero)
        numero = numero - int(entero)
        binario = binario + str(int(entero))
    return binario


def decToOctal(n):
    l_partes = str(n).split('.')
    n = int(l_partes[0])
    octalNum = [0] * 100
    i = 0
    octal = ""
    while (n != 0):
        octalNum[i] = n % 8
        n = int(n / 8)
        i += 1
    for j in range(i - 1, -1, -1):
        octal += str(octalNum[j])
    return octal


def decimalww(decimal):
    l_partes = str(decimal).split('.')
    decimal = l_partes[1]
    uwu = "0." + decimal
    numero = float(uwu)
    array = []
    for x in range(12):
        numero = numero * 8
        l_partes = str(numero).split('.')
        array.append(l_partes[0])
        numero = "0." + l_partes[1]
        numero = float(numero)
    x = "".join(str(e) for e in array)
    return x


def decToHexaInt(numero):
    hexa = hex(numero)
    hexa = hexa.upper()[2:]
    return hexa


def decToHexaFloat(numero):
    residuo2, entero2 = math.modf(float(numero))
    hexa2 = residuo2
    auxiliar = decToHexaInt(int(entero2))
    hexaDecimal = ""
    while len(hexaDecimal) <= 7:
        hexa2 = hexa2 * 16
        resi, entero = math.modf(hexa2)
        hexa2 = hexa2 - int(entero)
        hexaDecimal += decToHexaInt(int(entero))
    conversion = auxiliar + "." + hexaDecimal
    return conversion


# CALCULOS BASE OCTAL

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


# BINARIO A DECIMAL

def BinaDecimal(numero):
    numero = str(int(numero))
    decimal = int(numero, 2)
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


# CALCULOS BASE HEXADECIMAL

def HexaDecimalINT(numero):
    sistema = int(16)
    numint = int(str(numero), sistema)
    return numint  # retorna el total


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


# CONVERSIONES COMPLETA

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

    return render(request, 'resultadosConv/resultadoBinario.html',
                  {'numero': numero, 'decimal': numeroConvertidoDecimal,
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

    return render(request, 'resultadosConv/resultadoOctal.html', {'numero': numero, 'decimal': numeroConvertidoDecimal,
                                                                  'binario': numeroConvertidoBinario,
                                                                  'hexadecimal': numeroConvertidoHexa})


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

    return render(request, 'resultadosConv/resultadoHexadecimal.html',
                  {'numero': numero, 'decimal': numeroConvertidoDecimal,
                   'binario': numeroConvertidoBinario, 'octal': numeroConvertidoOctal})


def vistaResultadoDecimal(request):
    numero = request.POST['decimal']
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

    return render(request, 'resultadosConv/resultadoDecimal.html',
                  {'numero': numero, 'octal': numeroConvertidoOctal, 'binario': numeroConvertidoBinario,
                   'hexadecimal': numeroConvertidoHexa})


def vistaDerivadas(request):
    return render(request, "derivadas.html")


# ---------------------------------ECUACIONES NO LINEALES------------------------------------------

def vistaSolucion(request):
    x = symbols('x')  # Declarar variable independiente
    fun_escrita = request.POST['funcion']
    evaluador = float(request.POST['evaluar'])
    f = parse_expr(fun_escrita)
    funcionEval = sympy.sympify(f).subs(x, evaluador)
    dact = diff(f, x)
    derivada = str(simplify(dact))
    evaluada = sympy.sympify(derivada).subs(x, evaluador)

    dact2 = diff(f, x, 2)
    derivada2 = str(simplify(dact2))
    evaluada2 = sympy.sympify(derivada2).subs(x, evaluador)

    return render(request, 'derivadas.html',
                  {'f': funcionEval, 'derivada': derivada, 'derivada2': derivada2,
                   'evaluada': evaluada, 'evaluada2': evaluada2})


def secanteSolucion(request):
    f = request.POST['funcion']
    x0 = float(request.POST['x0'])
    x1 = float(request.POST['x1'])
    x0Pas = x0
    x1Pas = x1
    x0Salida = 0
    x1Salida = 0
    eMax = float(request.POST['eMax'])
    N = 100
    lista = []
    funcs = vars(math)
    for k in range(N):
        if x1 - x0 == 0:
            break
        x0Salida = x0
        x1Salida = x1
        fp = (eval(f, funcs, dict(x=x1)) - eval(f, funcs, dict(x=x0))) / (x1 - x0)

        x = x1 - eval(f, funcs, dict(x=x1)) / fp

        e = abs((x - x1) / x)
        if e < eMax:
            break
        x0 = x1
        x1 = x
        fx = eval(f, funcs, dict(x=x))
        lista.append([str(k + 1), str(x), str(x0), str(x1), str(e)])
        em = e
        xtot = x
    return render(request, 'resultadoSecante/secante.html',
                  {'f': f, 'x0': x0Pas, 'x1': x1Pas, 'eMax': eMax, 'raiz': xtot, 'error': str(em),
                   'fx': str(fx), 'lista': lista})


def vistaSecante(request):
    return render(request, "secante.html")


def vistatrapecio(request):
    return render(request, "Trapecio.html")


def vistaDecimal32(request):
    return render(request, "decimalABit32.html")


def vistaDecimalBit32(request):
    S = request.POST['signo']
    E = request.POST['exponente']
    M = request.POST['mantisa']
    N = S + E + M
    a = int(N[0])  # sign,     1 bit
    b = int(N[1:9], 2)  # exponent, 8 bits
    c = int("1" + N[9:], 2)  # fraction, len(N)-9 bits
    salida = (-1) ** a * c / (1 << (len(N) - 9 - (b - 127)))
    return render(request, 'decimalABit32.html',
                  {'salida': salida, 'signo': S, 'exponente': E, 'mantisa': M})


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
    salida = (-1) ** a * c / (1 << (len(N) - 12 - (b - 1023)))
    return render(request, 'decimalABit64.html',
                  {'salida': salida, 'signo': S, 'exponente': E, 'mantisa': M})


def vistaGraficar(request):
    return render(request, "graficas.html")


def f(expr, value):
    x = var('x')
    res = expr.subs(x, value)
    return res


def derivada(expr, value):
    x = Symbol('x')
    deriva = diff(expr, x)
    return deriva.subs(x, value)


def newton(expr, x_old):
    x = var('x')
    x_new = x_old - f(expr, x_old) / derivada(expr, x_old)
    return x_new


def vistaNewton(request):
    x = var('x')
    user_input = request.POST['funcion']
    expr = sympify(user_input)
    x_old = float(request.POST['x0'])
    x0Salida = x_old
    RAE = float(request.POST['error'])
    error = RAE
    RAE_now = 100
    counter = 0
    lista = []
    while RAE < RAE_now:
        x_new = newton(expr, x_old)
        selisih = abs(x_new - x_old)
        RAE_now = abs(selisih / x_new)
        x_old = x_new
        counter = counter + 1
        lista.append([counter, x_new, RAE_now])
    return render(request, 'resultadoSecante/newtonSolucion.html',
                  {'expr': expr, 'raiz': x_new, 'error': RAE_now, 'x0': x0Salida, 'error2': error,
                   'lista': lista})


def vistaNew(request):
    return render(request, "newton.html")


def raiznew(request):
    return render(request, "raicez_polisticas.html")


def vistabi(request):
    return render(request, "bisecion.html")


def vistaraicez_pro(request):
    numeric_const_pattern = r"""
    [-+]? # optional sign
     (?:
         (?: \d* \. \d+ ) # .1 .12 .123 etc 9.1 etc 98.1 etc
         |
         (?: \d+ \.? ) # 1. 12. 123. etc 1 12 123 etc
     )     # followed by optional exponent part if desired
     (?: [Ee] [+-]? \d+ ) ?
     """
    coeficientes = []
    ecuacion = request.POST["funcion"]
    exponentes = []
    for x in range(len(ecuacion)):
        if (ecuacion[x].isnumeric() == True and ecuacion[x - 1] == "*" and ecuacion[x - 2] == "*"):
            exponentes.append(ecuacion[x])
    rx = standardre.compile(numeric_const_pattern, standardre.VERBOSE)
    owo = rx.findall(ecuacion)
    position = False
    for x in range(len(exponentes)):
        if exponentes[x] in owo:
            owo.remove(exponentes[x])
    uwu = list(map(float, owo))
    return render(request, 'resultadoSecante/raizsolucion.html',
                  {'raiz': np.roots(uwu), 'f': ecuacion})


def bisecionr(request):
    i = 0
    lista = []
    func = request.POST['funcion']
    a = float(request.POST['a'])
    b = float(request.POST['b'])
    funcs = vars(math)
    error_aceptable = float(request.POST['error'])

    def f(x):
        f = eval(func)
        return f

    error = abs(b - a)
    while error > error_aceptable:
        c = (b + a) / 2

        if eval(func, funcs, dict(x=a)) * eval(func, funcs, dict(x=b)) >= 0:
            break

        elif eval(func, funcs, dict(x=c)) * eval(func, funcs, dict(x=a)) < 0:
            b = c
            error = abs(b - a)

        elif eval(func, funcs, dict(x=c)) * eval(func, funcs, dict(x=b)) < 0:
            a = c
            error = abs(b - a)
        else:
            mensaje = ("algo malo paso D:")
            break
        i = i + 1
        lista.append([i, a, error])
    return render(request, 'resultadoSecante/resultado_bisecion.html',
                  {'raiz': a, 'error': error, 'lista': lista})


def vistaposicion(request):
    n = 50
    fun = request.POST['funcion']
    a = float(request.POST['a'])
    b = float(request.POST['b'])
    tol = float(request.POST['error'])
    funcs = vars(math)
    lista = []
    auxiliar = ""
    mensaje = ""

    def f(x):
        f = eval(fun)
        return f

    if f(a) * f(b) >= 0:
        mensaje = ('El intervalo no funciona, f(a)={:.2f} y f(b)={:.2f}'.format(eval(fun, funcs, dict(x=a)),
                                                                                eval(fun, funcs, dict(x=b))))
    else:
        e_abs = abs(b - a)
        i = 1
        c = a - (eval(fun, funcs, dict(x=a)) * (b - a)) / eval(fun, funcs, dict(x=b)) - eval(fun, funcs, dict(x=a))

        while i <= n and e_abs > tol:

            c_1 = c

            lista.append([str(i), str(a), str(b), str(c_1)])

            if eval(fun, funcs, dict(x=c_1)) == 0:
                mensaje = ('Solución encontrada x={:.7f}'.format(c_1))
                auxiliar = c_1
                break

            if eval(fun, funcs, dict(x=a)) * eval(fun, funcs, dict(x=c)) < 0:
                b = c_1

            else:
                a = c_1

            c = a - (eval(fun, funcs, dict(x=a)) * (b - a)) / (
                        eval(fun, funcs, dict(x=b)) - eval(fun, funcs, dict(x=a)))
            e_abs = abs(c_1 - c)

            if e_abs < tol:
                mensaje = ('Solución encontrada x= {:.7f}, iteraciones: {}'.format(c, i))
                break
            else:
                mensaje = ('Solución no encontrada, iteraciones agotadas: {}'.format(i - 1))
            i += 1

    return render(request, 'resultadoSecante/solucionPosi.html',
                  {'lista': lista, 'mensaje': mensaje})


def vistaponew(request):
    return render(request, "falsaposi.html")


def TrapeNew(request):
    x = Symbol('x')
    funcs = vars(math)
    y = (9 - x * 2) * 1 / 2
    derivada = y.diff(x)
    funcs = vars(math)

    def f(x):
        f = eval(fun)
        return f

    fun = request.POST['funcion']
    n = int(request.POST['particiones'])
    a = float(request.POST['a'])
    b = float(request.POST['b'])
    Dx = (b - a) / n
    suma = 0
    delta = (float(b) - float(a)) / float(n)

    for i in range(n):
        area = (eval(fun, funcs, dict(x=a)) + eval(fun, funcs, dict(x=a + Dx))) * Dx / 2
        suma = suma + area
        a = a + Dx

    randomico = random.uniform(0, 1)
    simbolo = float(a) + randomico * (float(b) - float(a))
    derivadaG = float(sympy.diff(fun, x, 2).evalf(subs={x: simbolo}))
    error = ((-1) / 12) * (derivadaG) * (delta ** 3)
    return render(request, 'Trapecio.html',
                  {'fun': fun, 'n': n, 'suma': suma, 'error': error})


def calcular_derivada(fun, valor, num_int):
    fun = sympy.sympify(fun)
    x = sympy.symbols('x')
    numero = valor
    r_pd = float(sympy.diff(fun, x, num_int).evalf(subs={x: numero}))

    return r_pd


def vistaRectangulos(request):
    return render(request, "integralRectangulos.html")


def integrarRectangulosIzquierda(f, a, b, n):
    suma = 0
    funcs = vars(math)
    Dx = (b - a) / n
    for i in range(n):
        # POR LA DERECHA
        altura = eval(f, funcs, dict(x=a + Dx))
        area = Dx * altura
        suma = suma + area
        a = a + Dx
    return suma


def integrarRectangulosDerecha(f, a, b, n):
    suma = 0
    funcs = vars(math)
    Dx = (b - a) / n
    for i in range(n):
        # POR LA DERECHA
        altura = eval(f, funcs, dict(x=a))
        area = Dx * altura
        suma = suma + area
        a = a + Dx
    return suma


def integrarRectangulosMedio(f, a, b, n):
    suma = 0
    funcs = vars(math)
    Dx = (b - a) / n
    for i in range(n):
        # POR LA DERECHA
        altura = eval(f, funcs, dict(x=a + Dx / 2))
        area = Dx * altura
        suma = suma + area
        a = a + Dx
    return suma


def vistaRectangulosSolucion(request):
    fun = request.POST['funcion']
    limIn = float(request.POST['a'])
    limSup = float(request.POST['b'])
    nPart = int(request.POST['n'])
    solIzq = integrarRectangulosIzquierda(fun, limIn, limSup, nPart)
    solDer = integrarRectangulosDerecha(fun, limIn, limSup, nPart)
    solMed = integrarRectangulosMedio(fun, limIn, limSup, nPart)
    return render(request, 'integralRectangulos.html',
                  {'f': fun, 'limIn': limIn, 'nPart': nPart, 'limSup': limSup, 'solIzq': solIzq, 'solDer': solDer,
                   'solMed': solMed})


def vistaSimpson(request):
    return render(request, "Simpson.html")


def Simpson13(f, a, b, n):
    funcs = vars(math)

    def evaluacion(x):
        copia = f.copy()
        for j in range(len(copia)):
            if copia[j] == "x":
                copia[j] == x
        return eval("".join(copia))

    def simpson1_3(f, a, b):
        m = (a + b) / 2
        integral = (b - a) / 6 * (evaluacion(a) + 4 * evaluacion(m) + evaluacion(b))
        return integral

    h = (b - a) / n
    suma = 0
    for i in range(n):
        b = a + h
        area = simpson1_3(f, a, b)
        suma = suma + area
        a = b
    return suma


def Simpson_error(f, a, b, n):
    funcs = vars(math)
    h = (b - a) / n
    n_random = random.uniform(0, 1)
    ep = a + n_random * (b - a)
    str1 = ''.join(f)
    str2 = str1.replace('math.', '')
    derivada = calcular_derivada(str2, float(ep), 4)
    error = -((3 / 80) * (h ** 5) * derivada)

    return error


def Simpson38(f, a, b, n):
    funcs = vars(math)

    def funcion(x):
        copia = f.copy()
        for j in range(len(copia)):
            if copia[j] == "x":
                copia[j] == x
        return eval("".join(copia))

    def sinson(fx, ax, bx):
        m1 = (2 * ax + bx) / 3
        m2 = (ax + 2 * bx) / 3
        integral = (bx - ax) / 8 * (funcion(ax) + 3 * funcion(m1) + 3 * funcion(m2) + funcion(bx))
        return integral

    h = (b - a) / n
    suma = 0
    for i in range(n):
        b = a + h
        area = sinson(f, a, b)
        suma = suma + area
        a = b

    return suma


def vistaSimpsonSolucion(request):
    funcion = request.POST['funcion']
    fun = list(funcion)
    limIn = float(request.POST['a'])
    limSup = float(request.POST['b'])
    nPart = int(request.POST['n'])
    solIzq = Simpson13(fun, limIn, limSup, nPart)
    solDer = Simpson38(fun, limIn, limSup, nPart)
    erroir1_3 = Simpson_error(fun, limIn, limSup, nPart)
    erroir3_8 = Simpson_error(fun, limIn, limSup, nPart)
    return render(request, 'Simpson.html',
                  {'f': funcion, 'limIn': limIn, 'nPart': nPart, 'limSup': limSup, 'solIzq': solIzq, 'solDer': solDer,
                   'errorcito': erroir1_3, 'errorsote': erroir3_8})


def vistaCarlo(request):
    return render(request, "integralCarlo.html")


def vistaCarloSolucion(request):
    x = Symbol('x')

    def func(x):
        func = eval(fun)
        return func

    funcs = vars(math)
    fun = request.POST['funcion']
    a = float(request.POST['a'])
    b = float(request.POST['b'])
    N = int(request.POST['n'])
    q = 0
    i = 0
    x = np.linspace(a, b, N)
    fmin = min(func(x))
    fmax = max(func(x))
    area = (b - a) * (fmax)
    xrand = np.random.uniform(a, b, N)
    yrand = np.random.uniform(fmin, fmax, N)

    while (i <= N):
        if (yrand[i - 1] <= func(xrand[i - 1])):
            q += 1
            if (i == N):
                break
            else:
                i += 1
        else:
            if (i == N):
                break
            else:
                i += 1

    valorIntegral = (np.sum(q) / N) * area

    return render(request, 'integralCarlo.html',
                  {'f': fun, 'limIn': a, 'nPart': N, 'limSup': b, 'valor': valorIntegral, 'num': q})


def vistaMatriz(request):
    return render(request, "matrices.html")


# operaciones basicas
def resta_matrix(matris1, matris2):
    return (np.around(matris1 - matris2, 4))


def suma_matrix(matris1, matris2):
    return (np.around(matris1 + matris2, 4))


def multiplicacion_matrix(matris1, matris2):
    return (np.around(np.dot(matris1, matris2), 4))


# joder operaciones complejas

def matrix_TRANSPUESTA(matris):
    return (np.around(np.transpose(matris), 4))


def matrix_DETERMINANTE(matris):
    matriz2 = np.linalg.det(matris)
    return (round(matriz2, 4))


def matrix_inversa(matris):
    matriz2 = np.linalg.inv(matris)
    return (np.around(matriz2, 4))


# vista de matricez no complejas

def vistaMatrix(request):
    return render(request, "matrix.html")


def vistamatrixSolucion(request):
    matris1 = str(request.POST['matris1'])
    matris2 = str(request.POST['matris2'])
    if ('sumar' in request.POST):
        matris = (suma_matrix(matris1, matris2))
    if ('restar' in request.POST):
        matris = (resta_matrix(matris1, matris2))
    if ('multiplicar' in request.POST):
        matris = (multiplicacion_matrix(matris1, matris2))
    return render(request, 'resultado_matrix/resultado_matrix.html',
                  {'matris_final': matris})


# vista de matricez  complejas

def vistaMatrixcompleja(request):
    return render(request, "matrix_compleja.html")


def vistaMatrixcomplejaSolucion(request):
    matris1 = str(request.POST['matris1'])
    if ('TRANSPUESTA' in request.POST):
        matris = (matrix_TRANSPUESTA(matris1))
    if ('DETERMINANTE' in request.POST):
        matris = (matrix_DETERMINANTE(matris1))
    if ('inversa' in request.POST):
        matris = (matrix_inversa(matris1))
    return render(request, 'resultado_matrix/resultado_matrix_compleja.html',
                  {'matris_final': matris})


def payment_method_ajax(request, method):  # method is your slug

    options = {
        'Generar': numberForm(request.GET),
        'Generar2': numberForm(request.GET),
    }

    if method in options.keys():
        context = {'form': options[method],
                   'form2': options[method]
                   }
    else:
        context = None

    template = 'form_from_ajax.html'
    return render(request, template, context)


def get_digits(request):
    global dicMatrices
    global agregadas
    global copiaMostrar
    global listaM
    if request.method == 'POST':

        form = numberForm(request.POST)
        if form.is_valid():

            try:

                numbers = form.cleaned_data['numbers']
                m = form.cleaned_data['rows']
                n = form.cleaned_data['cols']
                nom = request.POST['nom']
                num_array = list(numbers)

                A = num_array
                A = np.array(A).reshape(m, n)
                dicMatrices.update({nom: A})

                P_rows = A.shape[0]
                P_cols = A.shape[1]

                # Parallel arrays hold numerator and denominators
                P_list = [None] * (P_rows * P_cols)
                P_numr = [None] * (P_rows * P_cols)
                P_dnmr = [None] * (P_rows * P_cols)

                counter = 0

                for i in range(P_rows):
                    for j in range(P_cols):
                        P_numr[counter] = A[i, j]
                        P_dnmr[counter] = 1
                        counter += 1

                # Zip arrays for template rendering
                P_zip = zip(P_numr, P_dnmr)
                agregadas.append([A, A.shape[0], A.shape[1]])
                listaM.update({P_cols: P_zip})

                form = numberForm()
                # Invalid output response: something went wrong within the calculation
                return render(request, 'matrix.html', {
                    'form': form, 'lista': dicMatrices, 'anterior': copiaMostrar, 'agregadas': agregadas,
                    'listaM': listaM})
            except:
                form = numberForm()
                return render(request, 'matrix.html', {
                    'form': form, 'lista': dicMatrices, 'anterior': copiaMostrar, 'agregadas': agregadas,
                    'listaM': listaM
                })
        else:
            valid_output = False
            out = 'revisa tu matriz'
            form = numberForm()
            return render(request, 'matrix.html', {
                'form': form,
            })

    else:

        form = numberForm()

        return render(request, 'matrix.html', {
            'form': form, 'lista': dicMatrices, 'anterior': copiaMostrar, 'agregadas': agregadas, 'listaM': listaM
        })


def operaciones(request):
    global dicMatrices
    global agregadas
    global copiaMostrar
    global listaM
    form = numberForm()
    validez = True
    mostrar = 1
    mensaje = ""
    P_rows = 0
    P_cols = 0
    P_zip = 0

    matrizUno = request.POST.get('matriz1')
    matriz1 = dicMatrices.get(matrizUno)

    matrizDos = request.POST.get('matriz2')
    matriz2 = dicMatrices.get(matrizDos)

    nom = request.POST['nom2']

    if ('sumar' in request.POST):
        if matriz1.shape[0] == matriz2.shape[0] and matriz1.shape[1] == matriz2.shape[1]:
            matris = (suma_matrix(matriz1, matriz2))
        else:
            matris = matriz1
            validez = False
            mensaje = "Las matrices deben tener el mismo tamaño, la misma cantidad de columnas y de filas."

    if ('restar' in request.POST):
        if matriz1.shape[0] == matriz2.shape[0] and matriz1.shape[1] == matriz2.shape[1]:
            matris = (resta_matrix(matriz1, matriz2))
        else:
            matris = matriz1
            validez = False
            mensaje = "Las matrices deben tener el mismo tamaño, la misma cantidad de columnas y de filas."

    if ('multiplicar' in request.POST):
        if matriz1.shape[1] == matriz2.shape[0]:
            matris = (multiplicacion_matrix(matriz1, matriz2))
        else:
            matris = matriz1
            validez = False
            mensaje = "El número de columnas de la primera matriz debe coincidir con el número de filas de la segunda matriz."

    if validez == True:
        dicMatrices.update({nom: matris})

        P_rows = matris.shape[0]
        P_cols = matris.shape[1]

        # Parallel arrays hold numerator and denominators
        P_list = [None] * (P_rows * P_cols)
        P_numr = [None] * (P_rows * P_cols)
        P_dnmr = [None] * (P_rows * P_cols)

        counter = 0
        for i in range(P_rows):
            for j in range(P_cols):
                P_numr[counter] = matris[i, j]
                P_dnmr[counter] = 1
                counter += 1

        P_zip = zip(P_numr, P_dnmr)
        listaM.update({P_cols: P_zip})
        agregadas.append([matris, matris.shape[0], matris.shape[1]])

    return render(request, 'matrix.html',
                  {'matriz': matris, 'form': form, 'lista': dicMatrices, 'resultado': matris, 'nombre': nom,
                   'mostrar': mostrar, 'P_zip': P_zip, 'P_rows': P_rows, 'P_cols': P_cols,
                   'validez': validez, 'mensaje': mensaje, 'anterior': copiaMostrar, 'agregadas': agregadas,
                   'listaM': listaM})


def operaciones2(request):
    global dicMatrices
    global agregadas
    global copiaMostrar
    global listaM
    form = numberForm()
    validez = True
    mostrar = 2
    noMatriz = 2
    mensaje = ""
    matrizUno = str(request.POST.get('matrizU'))
    matriz1 = dicMatrices.get(matrizUno)

    nom = request.POST['nom3']

    if ('TRANSPUESTA' in request.POST):
        matris = (matrix_TRANSPUESTA(matriz1))

    if ('DETERMINANTE' in request.POST):
        if matriz1.shape[0] != matriz1.shape[1]:
            matris = matriz1
            validez = False
            mensaje = "La matriz no es cuadrada."
        else:

            noMatriz = 1
            matris = (matrix_DETERMINANTE(matriz1))
    if ('inversa' in request.POST):
        if matriz1.shape[0] != matriz1.shape[1]:
            matris = matriz1
            validez = False
            mensaje = "La matriz no es cuadrada."
        else:
            det = (matrix_DETERMINANTE(matriz1))
            if det == 0:
                matris = matriz1
                validez = False
                mensaje = "El determinante de la matriz es 0, la matriz es no invertible"
            else:
                matris = (matrix_inversa(matriz1))

    if noMatriz == 1:

        P_rows = matriz1.shape[0]
        P_cols = matriz1.shape[1]

        # Parallel arrays hold numerator and denominators
        P_list = [None] * (P_rows * P_cols)
        P_numr = [None] * (P_rows * P_cols)
        P_dnmr = [None] * (P_rows * P_cols)

        counter = 0

        for i in range(P_rows):
            for j in range(P_cols):
                P_numr[counter] = matriz1[i, j]
                P_dnmr[counter] = 1
                counter += 1

        # Zip arrays for template rendering
        P_zip = zip(P_numr, P_dnmr)

    else:

        P_rows = matris.shape[0]
        P_cols = matris.shape[1]

        # Parallel arrays hold numerator and denominators
        P_numr = [None] * (P_rows * P_cols)
        P_dnmr = [None] * (P_rows * P_cols)

        counter = 0

        for i in range(P_rows):
            for j in range(P_cols):
                P_numr[counter] = matris[i, j]
                P_dnmr[counter] = 1
                counter += 1

        # Zip arrays for template rendering
        P_zip = zip(P_numr, P_dnmr)
        if validez == True:
            listaM.update({P_cols: P_zip})
            dicMatrices.update({nom: matris})
            agregadas.append([matris, matris.shape[0], matris.shape[1]])

    return render(request, 'matrix.html',
                  {'matriz': matriz1, 'form': form, 'lista': dicMatrices, 'resultado': matris, 'nombre': nom,
                   'mostrar': mostrar,
                   'validez': validez, 'noMatriz': noMatriz, 'P_zip': P_zip, 'P_rows': P_rows, 'P_cols': P_cols,
                   'mensaje': mensaje,
                   'anterior': copiaMostrar, 'agregadas': agregadas, 'listaM': listaM})


def matrix_reescalacion(numero, matris):
    matriz1 = matris * numero
    return np.around(matriz1, 4)


def matrix_elevada(numero, matris):
    matriz1 = np.linalg.matrix_power(matris, numero)
    return np.around(matriz1, 4)


def operaciones3(request):
    global dicMatrices
    global agregadas
    global copiaMostrar
    global listaM
    form = numberForm()
    validez = True
    mostrar = 3
    noMatriz = 2
    mensaje = ""
    P_rows = 0
    P_cols = 0
    P_zip = 0

    matrizUno = str(request.POST.get('matrizD'))
    matriz1 = dicMatrices.get(matrizUno)

    numero = request.POST['numero']
    nom = request.POST['nom4']

    if ('Elevado' in request.POST):
        if matriz1.shape[0] != matriz1.shape[1]:
            matris = matriz1
            validez = False
            mensaje = "La matriz no es cuadrada."
        else:
            matris = (matrix_elevada(int(numero), matriz1))
    if ('Escalar' in request.POST):
        matris = (matrix_reescalacion(float(numero), matriz1))

    if validez == True:

        dicMatrices.update({nom: matris})
        agregadas.append([nom, matris])
        P_rows = matris.shape[0]
        P_cols = matris.shape[1]

        # Parallel arrays hold numerator and denominators
        P_list = [None] * (P_rows * P_cols)
        P_numr = [None] * (P_rows * P_cols)
        P_dnmr = [None] * (P_rows * P_cols)

        counter = 0

        for i in range(P_rows):
            for j in range(P_cols):
                P_numr[counter] = matris[i, j]
                P_dnmr[counter] = 1
                counter += 1

        # Zip arrays for template rendering
        P_zip = zip(P_numr, P_dnmr)
        listaM.update({P_cols: P_zip})
        agregadas.append([matris, matris.shape[0], matris.shape[1]])

    return render(request, 'matrix.html',
                  {'matriz': matriz1, 'form': form, 'lista': dicMatrices, 'resultado': matris, 'nombre': nom,
                   'mostrar': mostrar,
                   'validez': validez, 'noMatriz': noMatriz, 'P_zip': P_zip, 'P_rows': P_rows, 'P_cols': P_cols,
                   'mensaje': mensaje, 'anterior': copiaMostrar, 'agregadas': agregadas, 'listaM': listaM})


def mostrar_form_ajuste_de_curvas(request):
    global resultado_a_c
    return render(request, 'form_ajuste_curvas.html', {'result': resultado_a_c})


def resolver_ajuste_curvas(request):
    boton = request.POST['calcular']
    global resultado_a_c
    if boton == 'Borrar':
        limpiar_respuesta()
    elif boton == 'calcular':
        x = request.POST['x']
        solx = ordenar_arreglo(x)
        y = request.POST['y']
        soly = ordenar_arreglo(y)
        n = len(solx)
        resultado_a_c = solucionar_ajuste_curvas(solx, soly, n)
    return redirect('mostrar_form_ajuste_de_curvas')


def ordenar_2(msj):
    lista = msj.split(sep='\r\n')
    lista_final = []
    for x in lista:
        lista_final.append(x)
    return lista_final


def to_matriz(msj):
    mat = []
    for x in msj:
        fila = x.split(sep=' ')
        mat.append(fila)
    return mat


def to_float(msj):
    mat = []
    aux = []
    for x in msj:
        for y in x:
            aux.append(float(y))
        mat.append(aux.copy())
        aux.clear()
    return mat


def ordenar_arreglo(msj):
    lista = msj.split(sep=',')
    lista_final = []
    for x in lista:
        lista_final.append(float(x))
    return lista_final


def limpiar_respuesta():
    global resultado_a_c
    resultado_a_c.clear()


def determinar_func(func, valor):
    ecuacion = sympy.sympify(func)
    simbolo = sympy.symbols('x')
    result = ecuacion.evalf(subs={simbolo: float(valor)})
    return result


def hallar_media_y(y):
    suma = 0
    promedio = 0
    for x in y:
        suma += x
    promedio = int(suma / len(y))
    return promedio


def hallar_st(y):
    media = hallar_media_y(y)
    sumatoria = 0
    for i in y:
        sumatoria += pow((i - media), 2)
    return sumatoria


def hallar_sr(funcion, x, y):
    sumatoria = 0
    for i in range(len(x)):
        sumatoria += pow(y[i] - determinar_func(funcion, x[i]), 2)
    return sumatoria


def sumatoria(arreglo, exp):
    suma = 0
    for a in arreglo:
        suma = suma + pow(a, exp)

    return suma


def sumatoria_y(expo, x, y):
    suma = 0
    for i in range(len(x)):
        suma += pow(x[i], expo) * y[i]
    return suma


def resultado_y(x, y):
    sumar = []
    for d in range(7):
        sumar.append(sumatoria_y(d, x, y))
    return np.array(sumar)


def get_respuesta(vec, mat):
    res = []
    for c in range(len(mat)):
        res.append(vec[c])
    return np.array(res)


def resolver_lineal(mat, vec):
    m = np.linalg.solve(mat, vec)
    return retornar_func(m)


def retornar_func(num):
    msj = ''
    for n in range(len(num)):
        if n == 0:
            msj += str('{:.9f}'.format(num[n])) + ' '
        else:
            if num[n] < 0:
                msj += str('{:.9f}'.format(num[n])) + '*x^' + str(n) + ' '
            else:
                msj += ' + ' + str('{:.9f}'.format(num[n])) + '*x^' + str(n) + ' '
    return msj


def resolver_ecuaciones_lineales(mat, vec):
    aux1 = []
    aux2 = []
    result = []
    for x in range(6):
        for m in range(len(mat)):
            aux1.append([get_respuesta(vec, mat[m]), mat[m]])
        if np.linalg.det(aux1[x][1]) != 0:
            aux2.append([x + 1, resolver_lineal(aux1[x][1], aux1[x][0])])
        else:
            aux2.append('el determinante de esta matriz es 0')
            return False
    return aux2


def solucionar_ajuste_curvas(x, y, n):
    respuestas = []
    vector = []
    aux = []
    result = []
    terminos_funcion = []
    conta = 8
    exponente = 0
    coeficiente = 0
    resultados = resultado_y(x, y)
    # me rellena todas las matrices.
    for i in range(2, conta):
        for f in range(i):
            for c in range(i):
                if c == 0 and f == 0:
                    aux.append(n)
                else:
                    aux.append(sumatoria(x, exponente))
                if c == i - 1:
                    respuestas.append(aux.copy())
                    aux.clear()
                    exponente = f
                exponente += 1

        vector.append(np.array(respuestas.copy()))
        respuestas.clear()
        exponente = 0

    final = resolver_ecuaciones_lineales(vector, resultados)
    if final != False:
        st = hallar_st(y)
        for t in range(len(final)):
            sr = hallar_sr(final[t][1], x, y)
            coeficiente = pow(((st - sr) / st), 0.5)
            final[t].append(coeficiente)

        return final
    else:
        return []


def get_digits2(request):
    global dicMatrices
    global agregadas
    global copiaMostrar
    global listaM
    if request.method == 'POST':

        form = numberForm(request.POST)
        if form.is_valid():

            try:

                numbers = form.cleaned_data['numbers']
                m = form.cleaned_data['rows']
                n = form.cleaned_data['cols']
                num_array = (list(numbers))

                A = num_array
                A = np.array(A).reshape(m, n)

                gausito = gaus_jordan(A)
                lista = []
                P_rows = A.shape[0]
                P_cols = A.shape[1]
                # Parallel arrays hold numerator and denominators
                P_list = [None] * (P_rows * P_cols)
                P_numr = [None] * (P_rows * P_cols)
                P_dnmr = [None] * (P_rows * P_cols)

                counter = 0

                for i in range(P_rows):
                    for j in range(P_cols):
                        P_numr[counter] = A[i, j]
                        P_dnmr[counter] = 1
                        counter += 1

                # Zip arrays for template rendering
                P_zip = zip(P_numr, P_dnmr)
                agregadas.append([A, A.shape[0], A.shape[1]])
                listaM.update({P_cols: P_zip})

                form = numberForm()
                # Invalid output response: something went wrong within the calculation
                return render(request, 'Gauss.html', {
                    'form': form, 'gausito': gausito})
            except:
                form = numberForm()
                return render(request, 'Gauss.html', {
                    'form': form, 'lista': dicMatrices, 'anterior': copiaMostrar, 'agregadas': agregadas,
                    'listaM': listaM
                })
        else:
            valid_output = False
            out = 'revisa tu matriz'
            form = numberForm()
            return render(request, 'Gauss.html', {
                'form': form,
            })

    else:

        form = numberForm()

        return render(request, 'Gauss.html', {
            'form': form, 'lista': dicMatrices, 'anterior': copiaMostrar, 'agregadas': agregadas, 'listaM': listaM
        })


def gaus_jordan(numpy_array):
    np_list = numpy_array.tolist()
    ecuaciones = len(np_list)
    variables = len(np_list[0])
    listaMatriz = []
    vector = np.zeros((ecuaciones))
    for idx in range(ecuaciones):
        for idm in range(variables):
            if (idm == variables - 1):
                vector[(idx)] = np_list[idx][idm]
            else:
                listaMatriz.append(np_list[idx][idm])

    matriz = np.array(listaMatriz).reshape(ecuaciones, variables - 1)
    determinante = 0

    if determinante == 0 or ecuaciones != variables:
        solucion, residuals, rank, s = np.linalg.lstsq(matriz, vector, rcond=None)
    else:
        solucion = np.linalg.solve(matriz, vector)

    return solucion
