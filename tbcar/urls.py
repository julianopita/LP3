"""tbcar URL Configuration

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
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from core.views import home
from core.views import cadastroCliente
from core.views import listagemClientes
from core.views import cadastroVeiculo
from core.views import listagemVeiculos
from core.views import cadastroTabela
from core.views import listagemTabelas
from core.views import Registrar
from core.views import altera_cliente
from core.views import altera_veiculo
from core.views import altera_tabela
from core.views import exclui_cliente
from core.views import exclui_veiculo
from core.views import cadastroMensalista
from core.views import listagemMensalistas
from core.views import cadastroRotativo
from core.views import listagemRotativos
from core.views import altera_rotativo
from core.views import exclui_rotativo
from core.views import altera_mensalista
from core.views import exclui_mensalista
from core.views import cadastroMarca
from core.views import listagemMarcas
from core.views import altera_marca
from core.views import exclui_marca

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/registrar/', Registrar.as_view(), name='url_registrar'),
    path('captcha/', include('captcha.urls')),
    path('', home, name='url_principal'),
    path('cadastroCliente/', cadastroCliente, name='url_cadastro_cliente'),
    path('listaClientes/', listagemClientes, name='url_lista_clientes'),
    path('cadastroVeiculo/', cadastroVeiculo, name='url_cadastro_veiculo'),
    path('listagemVeiculos/', listagemVeiculos, name='url_listagem_veiculos'),
    path('cadastroTabela/', cadastroTabela, name='url_cadastro_tabela'),
    path('listagemTabelas/', listagemTabelas, name='url_listagem_tabelas'),
    path('altera_cliente/<int:id>/', altera_cliente, name='url_altera_cliente'),
    path('altera_veiculo/<int:id>/', altera_veiculo, name='url_altera_veiculo'),
    path('altera_tabela/<int:id>/', altera_tabela, name='url_altera_tabela'),
    path('exclui_cliente/<int:id>/', exclui_cliente, name="url_exclui_cliente"),
    path('exclui_veiculo/<int:id>/', exclui_veiculo, name="url_exclui_veiculo"),
    path('cadastroMensalista/', cadastroMensalista, name='url_cadastro_mensalista'),
    path('listagemMensalistas/', listagemMensalistas, name='url_listagem_mensalistas'),
    path('cadastroRotativo/', cadastroRotativo, name='url_cadastro_rotativo'),
    path('listagemRotativos/', listagemRotativos, name='url_listagem_rotativos'),
    path('altera_mensalista/<int:id>/', altera_mensalista, name='url_altera_mensalista'),
    path('exclui_mensalista/<int:id>/', exclui_mensalista, name="url_exclui_mensalista"),
    path('altera_rotativo/<int:id>/', altera_rotativo, name='url_altera_rotativo'),
    path('exclui_rotativo/<int:id>/', exclui_rotativo, name="url_exclui_rotativo"),
    path('listagemMarcas/', listagemMarcas, name="url_listagem_marcas"),
    path('cadastroMarca/', cadastroMarca, name="url_cadastro_marca"),
    path('altera_marca/<int:id>/', altera_marca, name="url_altera_marca"),
    path('exclui_marca/<int:id>/', exclui_marca, name="url_exclui_marca"),
    ]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)