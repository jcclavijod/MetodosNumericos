from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('32Bits/',views.vista32Bits, name='32Bits'),
    path('32BitsAccion/',views.vista32, name='32BitsAccion'),
    path('64Bits/',views.vista64Bits, name='64Bits'),
    path('64BitsAccion/',views.vista64, name='64BitsAccion'),
    #path('Decimal/',views.vistaDecimal, name='decimal'),
    #path('Binario/',views.vistaBinaria, name='binario'),
    #path('Hexadecimal/',views.vistaHexadecimal, name='hexadecimal'),
    #path('resultadoOctal/',views.vistaResultadoOctal, name='resultadoOctal'),
    #path('resultadoBinario/',views.vistaResultadoBinario, name='resultadoBinario'),
    #path('resultadoDecimal/',views.vistaResultadoDecimal, name='resultadoDecimal'),
    #path('resultadoHexadecimal/',views.vistaResultadoHexadecimal, name='resultadoHexadecimal'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)