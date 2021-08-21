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
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)