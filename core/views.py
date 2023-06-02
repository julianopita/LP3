from django.shortcuts import render, redirect
from core.forms import FormCliente, FormVeiculo, FormTabela, FormMensalista, FormRotativo, FormMarca
from core.models import Cliente, Marca, Veiculo, Tabela, Mensalista, Rotativo
from django.contrib.auth.decorators import login_required
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib import messages


def home(request):
    contexto={'home':'home'}
    return render(request, 'core/index.html', contexto)



@login_required
def altera_cliente(request, id):
    if request.user.is_staff:
        obj = Cliente.objects.get(id=id)
        form = FormCliente(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                messages.success(request, 'Dados do cliente alterados com sucesso!')
                return redirect('url_lista_clientes')
        contexto = {'form': form, 'txt_titulo': 'EditCliente', 'tct_descrição': "Altera Cliente"}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


def exclui_cliente(request, id):
    obj = Cliente.objects.get(id=id)
    contexto = {'text_info': obj.nome, 'txt_url': '/listaClientes/'}
    if request.POST:
        obj.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        contexto.update({'txt_tipo': 'listaClientes'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


def exclui_veiculo(request, id):
    obj = Veiculo.objects.get(id=id)
    contexto = {'txt_info': obj.placa, 'txt_url': '/listagemVeiculos/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo': 'listaVeiculos'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def altera_veiculo(request, id):
    if request.user.is_staff:
        obj = Veiculo.objects.get(id=id)
        form = FormVeiculo(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_veiculos')
        contexto = {'form': form, 'txt_titulo': 'EditVeiculo', 'tct_descrição': "Altera Veículo"}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


class Registrar(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('url_principal')
    template_name = 'registration/registrar.html'


@login_required
def cadastroCliente(request):
    if request.user.is_staff:
        form = FormCliente(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('url_lista_clientes')
        contexto = {'form': form, 'txt_titulo': 'cad_cli', 'txt_descricao': 'Cadastro de Cliente'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemClientes(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Cliente.objects.filter(nome__icontains=request.POST['input_pesquisa'])
        else:
            dados = Cliente.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite o nome do cliente', 'listagem':'listagem'}
        return render(request, 'core/listagem_clientes.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroVeiculo(request):
    if request.user.is_staff:
        form = FormVeiculo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_veiculos')
        contexto = {'form': form, 'txt_titulo': 'cad_veic', 'txt_descricao': 'Cadastro de Veículo'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemVeiculos(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Veiculo.objects.filter(placa__icontains=request.POST['input_pesquisa'])
        else:
            dados = Veiculo.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a placa do veículo','listagem':'listagem'}
        return render(request, 'core/listagem_veiculos.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroTabela(request):
    if request.user.is_staff:
        form = FormTabela(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_listagem_tabelas')
        contexto = {'form': form, 'txt_titulo': 'cad_vtab', 'txt_descricao': 'Cadastro de Tabela'}
        return render(request, 'core/cadastro.html')
    return render(request, 'aviso.html')


@login_required
def listagemTabelas(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Tabela.objects.filter(descricao__icontains=request.POST['input_pesquisa'])
        else:
            dados = Tabela.objects.all()
            contexto = {'dados': dados, 'text_input': 'Digite a descrição', 'listagem':'listagem'}
        return render(request, 'core/listagem_tabelas.html', contexto)
    return render(request, 'aviso.html')


@login_required
def altera_tabela(request, id):
    if request.user.is_staff:
        obj = Tabela.objects.get(id=id)
        form = FormTabela(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_tabelas')
        contexto = {'form': form, 'txt_titulo': 'EditTabela', 'tct_descrição': "Altera Tabela"}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroMensalista(request):
    if request.user.is_staff:
        form = FormMensalista(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_cadastro_mensalista')
        contexto = {'form': form, 'txt_titulo': 'cad_veic', 'txt_descricao': 'Cadastro de Mensalista'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemMensalistas(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Mensalista.objects.filter(id_veiculo__icontains=request.POST['input_pesquisa'])
        else:
            dados = Mensalista.objects.all()
            contexto = {'dados': dados, 'text_input': 'Digite a placa do veículo', 'listagem':'listagem'}
        return render(request, 'core/listagem_mensalistas.html', contexto)
    return render(request, 'aviso.html')


@login_required
def cadastroRotativo(request):
    if request.user.is_staff:
        form = FormRotativo(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_cadastro_rotativo')
        contexto = {'form': form, 'txt_titulo': 'cad_veic', 'txt_descricao': 'Cadastro de Rotativo'}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemRotativos(request):
    if request.user.is_staff:
        if request.POST and request.POST['input_pesquisa']:
            dados = Rotativo.objects.filter(id_veiculo__icontains=request.POST['input_pesquisa'])
        else:
            dados = Rotativo.objects.all()
            contexto = {'dados': dados, 'text_input': 'Digite a placa do veículo','listagem':'listagem'}
        return render(request, 'core/listagem_rotativos.html', contexto)
    return render(request, 'aviso.html')


@login_required
def altera_rotativo(request, id):
    if request.user.is_staff:
        obj = Rotativo.objects.get(id=id)
        form = FormRotativo(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                obj.calcula_total()
                form.save()
                return redirect('url_listagem_rotativos')
        contexto = {'form': form, 'txt_titulo': 'AltRot', 'tct_descrição': "Altera Rotativo"}
        return render(request, 'core/cadastro_rotativo_dividido.html', contexto)
    return render(request, 'aviso.html')


def exclui_rotativo(request, id):
    obj = Rotativo.objects.get(id=id)
    contexto = {'txt_info': f'{obj.id_veiculo}-{obj.entrada}', 'txt_url': '/listagemRotativos/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo': 'listaRotativos'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def altera_mensalista(request, id):
    if request.user.is_staff:
        obj = Mensalista.objects.get(id=id)
        form = FormMensalista(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_mensalistas')
        contexto = {'form': form, 'txt_titulo': 'AltRot', 'tct_descrição': "Altera Mensalista"}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


def exclui_mensalista(request, id):
    obj = Mensalista.objects.get(id=id)
    contexto = {'txt_info': f'{obj.id_veiculo}-{obj.entrada}', 'txt_url': '/listagemMensalistas/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo': 'listaMensalistas'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)


@login_required
def cadastroMarca(request):
    if request.user.is_staff:
        form = FormMarca(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('url_principal')
        contexto = {'form': form, 'txt_titulo': 'cad_mar', 'txt_descricao': 'Cadastro de Marca'}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def listagemMarcas(request):
    if request.user.is_staff:
        dados = Marca.objects.all()
        contexto = {'dados': dados, 'text_input': 'Digite a marca','listagem':'listagem'}
        return render(request, 'core/listagem_marcas.html', contexto)
    return render(request, 'aviso.html')


@login_required
def altera_marca(request, id):
    if request.user.is_staff:
        obj = Marca.objects.get(id=id)
        form = FormMarca(request.POST or None, request.FILES or None, instance=obj)
        if request.POST:
            if form.is_valid():
                form.save()
                return redirect('url_listagem_marcas')
        contexto = {'form': form, 'txt_titulo': 'AltMar', 'txt_descrição': "Altera Marca"}
        return render(request, 'core/cadastro.html', contexto)
    return render(request, 'aviso.html')


@login_required
def exclui_marca(request, id):
    obj = Marca.objects.get(id=id)
    contexto = {'txt_info': obj.nome, 'txt_url': '/listagemMarcas/'}
    if request.POST:
        obj.delete()
        contexto.update({'txt_tipo': 'listagemMarcas'})
        return render(request, 'core/aviso_exclusao.html', contexto)
    else:
        return render(request, 'core/confirma_exclusao.html', contexto)
