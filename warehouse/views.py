import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout

from warehouse.models import DimensionModel, GradeModel
from warehouse.forms import DimensionForm, LoginForm, GradeForm


def index(request):
    return render(request, 'index.html', {'form': LoginForm()})


# USER --------------------------------------------------------------------------------------------------------

def login_check(request):
    if request.user.is_authenticated:
        return redirect('panel')
    else:
        messages.add_message(request, messages.ERROR, 'Strona wymaga zalogowania')
        return redirect('index')


def login_user(request):
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
                return redirect('index')
    else:
        form = LoginForm()
        return render(request, 'authentication/login.html', context={'form': form})


def logout_user(request):
    logout(request)
    request.user = None
    messages.add_message(request, messages.SUCCESS, 'Wylogowano!')
    return redirect('index')


@login_required(login_url='/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def panel(request):
    return render(request, 'panel.html')


# DIMENSIONS ---------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def dimension_index(request):
    return render(request, 'dimension/main.html')


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


# GRADES ---------------------------------------------------------------------------------------------------

@login_required(login_url='/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def grade_index(request):
    return render(request, 'grade/main.html')


def grade_list(request):
    return render(request, 'grade/list.html', {'grade_list': GradeModel.objects.all()})


def grade_add(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Dodano gatunek: {grade.name}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "gradeListChanged": None
                    })

                })
    else:
        form = GradeForm()
    return render(request, 'grade/form.html', {
        'form': form,
    })


def grade_edit(request, pk):
    grade = get_object_or_404(GradeModel, pk=pk)
    if request.method == "POST":
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Zmieniono gatunek na {grade.name}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "gradeListChanged": None
                    })
                }
            )
    else:
        form = GradeForm(instance=grade)
    return render(request, 'grade/form.html', {
        'form': form,
        'grade': grade,
    })


def grade_remove(request, pk):
    grade = get_object_or_404(GradeModel, pk=pk)
    grade.delete()
    messages.add_message(request,
                         messages.SUCCESS,
                         f"Usunięto gatunek {grade.name}"
                         )
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "gradeListChanged": None
            })
        }
    )


# HEATS -----------------------------------------------------------------------------------------------------------
