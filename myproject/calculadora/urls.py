from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

urlpatterns = [
    path('',views.vistaIndex, name='inicio'),
    path('Octal/',views.vistaOctal, name='octal'),
    path('Decimal/',views.vistaDecimal, name='decimal'),
    path('Binario/',views.vistaBinaria, name='binario'),
    path('Hexadecimal/',views.vistaHexadecimal, name='hexadecimal'),
    path('resultadoOctal/',views.vistaResultadoOctal, name='resultadoOctal'),
    path('resultadoBinario/',views.vistaResultadoBinario, name='resultadoBinario'),
    path('resultadoDecimal/',views.vistaResultadoDecimal, name='resultadoDecimal'),
    path('resultadoHexadecimal/',views.vistaResultadoHexadecimal, name='resultadoHexadecimal'),
    path('iee/', include('estandarIEE.urls')),
    path('ecu/', include('ecuaciones.urls')),
    path('derivadas/', views.vistaDerivadas, name='derivadas'),
    path('derivadasSolucion/',views.vistaSolucion, name='derivadasSolucion'),
    path('secante/', views.vistaSecante, name='secante'),
    path('secanteSolucion/',views.secanteSolucion, name='secanteSolucion'),
    path('decimal32/', views.vistaDecimal32, name='decimal32'),
    path('decimalABit32/',views.vistaDecimalBit32, name='decimalABit32'),
    path('decimal64/', views.vistaDecimal64, name='decimal64'),
    path('decimalABit64/',views.vistaDecimalBit64, name='decimalABit64'),
    path('graficar/', views.vistaGraficar, name='graficar'),
    path('newtonR/',views.vistaNewton, name='newtonR'),
    path('newton/',views.vistaNew, name='newton'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)