from django.urls import path, include

from warehouse import views

urlpatterns = [
    # HOME / PANEL
    path('', views.index, name='index'),
    path('panel', views.panel, name='panel'),

    # LOGIN/LOGOUT
    path("login/", views.login_check, name="login"),
    path("login_user", views.login_user, name="login-user"),
    path("logout", views.logout_user, name="logout"),

    # DIMENSION
    path('dimension/all', views.dimension_index, name='dimension-main'),
    path('dimension/list', views.dimension_list, name='dimension-list'),
    path('dimension/add', views.dimension_add, name='dimension-add'),
    path('dimension/<int:pk>/edit', views.dimension_edit, name='dimension-edit'),
    path('dimension/<int:pk>/remove', views.dimension_remove, name='dimension-remove'),

]
