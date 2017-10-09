from django.conf.urls import url

from sitio.views import index

urlpatterns = [
    url(r'^$',index ),
    # url(r'^idmed/(?P<idmed>[\w.@+-]+)$', ver_horarios, name='verhor'),
    # url(r'^horarios/(?P<idmed>[\w.@+-]+)$', asignar_horario, name='asignarhor'),
    # url(r'^eliminado/(?P<idmed>[\w.@+-]+)$', eliminar_horario, name='eliminarhor')
]