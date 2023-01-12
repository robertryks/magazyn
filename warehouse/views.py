import json
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.http.response import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control
from django.contrib.auth import authenticate, login, logout

from warehouse.models import DimensionModel, GradeModel, HeatModel, CertificateModel, SupplyModel
from warehouse.forms import DimensionForm, LoginForm, GradeForm, HeatForm, CertificateForm, SupplyForm


def index(request):
    return render(request, 'index.html', {'form': LoginForm()})


# region USER

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


# endregion

# region DIMENSION

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


# endregion

# region GRADE

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


# endregion

# region HEAT


@login_required(login_url='/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def heat_index(request):
    return render(request, 'heat/main.html')


def heat_list(request):
    return render(request, 'heat/list.html', {'heat_list': HeatModel.objects.all()})


def heat_add(request):
    if request.method == 'POST':
        form = HeatForm(request.POST)
        if form.is_valid():
            heat = form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Dodano gatunek: {heat.name}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "heatListChanged": None
                    })

                })
    else:
        form = HeatForm()
    return render(request, 'heat/form.html', {
        'form': form,
    })


def heat_edit(request, pk):
    heat = get_object_or_404(HeatModel, pk=pk)
    if request.method == "POST":
        form = HeatForm(request.POST, instance=heat)
        if form.is_valid():
            form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Zmieniono wytop na {heat.name}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "heatListChanged": None
                    })
                }
            )
    else:
        form = HeatForm(instance=heat)
    return render(request, 'heat/form.html', {
        'form': form,
        'heat': heat,
    })


def heat_remove(request, pk):
    heat = get_object_or_404(HeatModel, pk=pk)
    heat.delete()
    messages.add_message(request,
                         messages.SUCCESS,
                         f"Usunięto wytop {heat.name}"
                         )
    return HttpResponse(
        status=204,
        headers={
            'HX-Trigger': json.dumps({
                "heatListChanged": None
            })
        }
    )


# endregion

# region CERTIFICATE

@login_required(login_url='/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def certificate_index(request):
    return render(request, 'certificate/main.html')


def certificate_list(request):
    return render(request, 'certificate/list.html', {'certificate_list': CertificateModel.objects.all()})


def certificate_add(request):
    if request.method == 'POST':
        form = CertificateForm(request.POST)
        if form.is_valid():
            certificate = form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Dodano certyfikat: {certificate.name}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "certificateListChanged": None
                    })

                })
    else:
        form = HeatForm()
    return render(request, 'certificate/form.html', {
        'form': form,
    })


def certificate_edit(request, pk):
    certificate = get_object_or_404(CertificateModel, pk=pk)
    if request.method == "POST":
        form = CertificateForm(request.POST, instance=certificate)
        if form.is_valid():
            form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Zmieniono certyfikat na {certificate.name}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "certificateListChanged": None
                    })
                }
            )
    else:
        form = CertificateForm(instance=certificate)
    return render(request, 'certificate/form.html', {
        'form': form,
        'certificate': certificate,
    })


def certificate_remove(request, pk):
    certificate = get_object_or_404(CertificateModel, pk=pk)
    related_list = certificate.is_deletable()
    if related_list:
        messages.add_message(request,
                             messages.ERROR,
                             f"Certyfikat {certificate.name} jest w użyciu."
                             )
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "certificateListChanged": None
                })
            }
        )
    else:
        certificate.delete()
        messages.add_message(request,
                             messages.SUCCESS,
                             f"Usunięto certyfikat {certificate.name}"
                             )
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "certificateListChanged": None
                })
            }
        )


# endregion

# region SUPPLY

@login_required(login_url='/login')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def supply_index(request):
    return render(request, 'supply/main.html')


def supply_list(request):
    return render(request, 'supply/list.html', {'supply_list': SupplyModel.objects.all()})


def supply_add(request):
    if request.method == 'POST':
        form = SupplyForm(request.POST)
        if form.is_valid():
            supply = form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Dodano dostawę o numerze: {supply.number}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "supplyListChanged": None
                    })

                })
    else:
        form = SupplyForm()
    return render(request, 'supply/form.html', {
        'form': form,
    })


def supply_edit(request, pk):
    supply = get_object_or_404(SupplyModel, pk=pk)
    if request.method == "POST":
        form = SupplyForm(request.POST, instance=supply)
        if form.is_valid():
            form.save()
            messages.add_message(request,
                                 messages.SUCCESS,
                                 f"Zmieniono numer dostawy na {supply.number}"
                                 )
            return HttpResponse(
                status=204,
                headers={
                    'HX-Trigger': json.dumps({
                        "supplyListChanged": None
                    })
                }
            )
    else:
        form = SupplyForm(instance=supply)
    return render(request, 'supply/form.html', {
        'form': form,
        'supply': supply,
    })


def supply_remove(request, pk):
    supply = get_object_or_404(SupplyModel, pk=pk)
    related_list = supply.is_deletable()
    if related_list:
        messages.add_message(request,
                             messages.ERROR,
                             f"Dostawa o numerze {supply.number} jest w użyciu."
                             )
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "supplyListChanged": None
                })
            }
        )
    else:
        supply.delete()
        messages.add_message(request,
                             messages.SUCCESS,
                             f"Usunięto dostawę o numerze {supply.number}"
                             )
        return HttpResponse(
            status=204,
            headers={
                'HX-Trigger': json.dumps({
                    "supplyListChanged": None
                })
            }
        )
# endregion
