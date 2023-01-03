from django.urls import path

from warehouse.views import IndexView, message, DimensionListView, DimensionCreateView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),

    # DIMENSION
    path('dimensions/show/', DimensionListView.as_view(), name='dimension-list'),
    path('dimensions/create/', DimensionCreateView.as_view(), name='dimension-create'),

    # OTHER
    path('message', message, name='message'),
]