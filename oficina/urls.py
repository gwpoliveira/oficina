from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('usuarios/', include('usuarios.urls', namespace='usuarios')),
    path('servicos/', include('servicos.urls', namespace='servicos')),
    path('', include('geral.urls', namespace='geral')),
]
