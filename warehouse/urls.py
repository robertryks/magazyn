from django.urls import path

from warehouse.views import IndexView, message, DimensionListView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dimensions/', DimensionListView.as_view(), name='dimension-list'),
    path('message', message, name='message'),
]