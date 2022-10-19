"""fomallhaut URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from projecto import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_views, name='login'),
    path('login_sistema/', views.login_sistema, name='login_sistema'),
    path('registro/', views.registro_views, name='registro'),
    path('registro_usuario/', views.registro_usuario),
    # path('admin/', admin.site.urls),
    path('perfilEstudiante/', views.perfilEstudiante_views, name='perfilEstudiante'),
    path('perfilProfesor/', views.perfilProfesor_views, name='perfilProfesor'),
    path('perfilAdministrador/', views.perfilAdministrador_views, name='perfilAdministrador'),
    path('registroGrupo/', views.registroGrupo_views, name='registroGrupo'),
    path('registroProyecto/', views.registroProyecto_views, name='registroProyecto'),
    # path('recuperarPass/', views.recuperarPass_views, name='recuperarPass'),
    # path('nuevaPass/', views.nuevaPass_views, name='nuevaPass')
]
