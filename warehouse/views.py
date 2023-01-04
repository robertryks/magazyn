import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


from warehouse.models import DimensionModel
from warehouse.forms import DimensionForm, LoginForm


def index(request):
    return render(request, 'index.html')


# USER --------------------------------------------------------------------------------------------------------

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, f'Witaj {user.username}! Zalogowano!')
                return redirect('panel')
            else:
                messages.add_message(request, messages.ERROR, 'Błąd logowania!')
    return render(request, 'authentication/login.html', context={'form': form})


def logout_user(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Wylogowano!')
    return redirect('index')


def panel(request):
    return render(request, 'panel.html')


# DIMENSIONS ---------------------------------------------------------------------------------------------------

def dimension_index(request):
    return render(request, 'dimension/index.html')


def dimension_list(request):
    return render(request, 'dimension/list.html', {'dimension_list': DimensionModel.objects.all()})


def dimension_add(request):
    if request.method == 'POST':
        form = DimensionForm(request.POST)
        if form.is_valid():
            dimension = form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Dodano średnicę {dimension.size} mm."
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "dimensionListChanged": None
                    })

                })
    else:
        form = DimensionForm()
    return render(request, 'dimension/form.html', {
        'form': form,
    })


def dimension_edit(request, pk):
    dimension = get_object_or_404(DimensionModel, pk=pk)
    if request.method == "POST":
        form = DimensionForm(request.POST, instance=dimension)
        if form.is_valid():
            form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Zmieniono średnicę na {dimension.size} mm."
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "dimensionListChanged": None
                    })
                }
            )
    else:
        form = DimensionForm(instance=dimension)
    return render(request, 'dimension/form.html', {
        'form': form,
        'dimension': dimension,
    })


def dimension_remove(request, pk):
    dimension = get_object_or_404(DimensionModel, pk=pk)
    dimension.delete()
    messages.add_message(request,
                         messages.SUCCESS,
                         f"Usunięto średnicę {dimension.size} mm."
                         )
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "dimensionListChanged": None
            })
        }
    )
