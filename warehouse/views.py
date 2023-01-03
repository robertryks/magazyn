import random
from django.shortcuts import render
from django.contrib import messages
from django.http.response import HttpResponse
from django.views.generic import View, ListView, CreateView

from warehouse.models import DimensionModel


class IndexView(View):
    template_name = 'index.html'

    def get(self, request):
        messages.add_message(request, messages.SUCCESS, 'Odświeżono stronę')
        context = {'info': 'Strona główna'}
        return render(request, self.template_name, context)


# DIMENSIONS ---------------------------------------------------------------------------------------------------

class DimensionListView(ListView):
    model = DimensionModel
    template_name = 'dimension/list.html'


class DimensionCreateView(CreateView):
    model = DimensionModel
    template_name = 'dimension/create.html'
    fields = ['size']
    success_url = 'dimensions/show/'


# POZOSTAŁE ----------------------------------------------------------------------------------------------------

SAMPLE_MESSAGES = [
    (messages.DEBUG, "Hello World!"),
    (messages.INFO, "System operational"),
    (messages.SUCCESS, "Congratulations! You did it."),
    (messages.WARNING, "Hum... not sure about that."),
    (messages.ERROR, "Oops! Something went wrong"),
]


def message(request):
    messages.add_message(request, *random.choice(SAMPLE_MESSAGES))
    return HttpResponse(status=204)
