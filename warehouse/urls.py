from django.urls import path, include

from warehouse import views

urlpatterns = [
    path('', views.index, name='index'),
    path("login", views.login_user, name="login"),
    path("logout", views.logout_user, name="logout"),
    path('panel', views.panel, name='panel'),

    # DIMENSION
    path('dimension/all', views.dimension_index, name='dimension-index'),
    path('dimension/list', views.dimension_list, name='dimension-list'),
    path('dimension/add', views.dimension_add, name='dimension-add'),
    path('dimension/<int:pk>/edit', views.dimension_edit, name='dimension-edit'),
    path('dimension/<int:pk>/remove', views.dimension_remove, name='dimension-remove'),

]
