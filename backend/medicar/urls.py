"""medicar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from clientes.views import ClienteView, MyAcountView
from especialidades.views import EspecialidadeView
from medicos.views import MedicoView
from agendas.views import AgendaView
from consultas.views import ConsultaList, ConsultaDetail


urlpatterns = [
    path('admin/', admin.site.urls),
    path('conta/login/', obtain_auth_token, name='api_token_auth'),
    path('conta/cadastrar/', ClienteView.as_view()),
    path('conta/minha-conta/', MyAcountView.as_view()),
    path('especialidades/', EspecialidadeView.as_view()),
    path('medicos/', MedicoView.as_view()),
    path('agendas/', AgendaView.as_view()),
    path('consultas/', ConsultaList.as_view()),
    path('consultas/<int:id>/', ConsultaDetail.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
