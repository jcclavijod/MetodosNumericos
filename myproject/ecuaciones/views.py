from django.shortcuts import render
import sympy
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from django.shortcuts import render, redirect
# Create your views here.

# DERIVADAS


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
                  {'derivada1': derivada, 'derivada1': derivada2,
                   'evaluada': evaluada, 'evaluada2': evaluada2})
