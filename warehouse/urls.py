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

    # GRADE
    path('grade/all', views.grade_index, name='grade-main'),
    path('grade/list', views.grade_list, name='grade-list'),
    path('grade/add', views.grade_add, name='grade-add'),
    path('grade/<int:pk>/edit', views.grade_edit, name='grade-edit'),
    path('grade/<int:pk>/remove', views.grade_remove, name='grade-remove'),

    # HEAT
    path('heat/all', views.heat_index, name='heat-main'),
    path('heat/list', views.heat_list, name='heat-list'),
    path('heat/add', views.heat_add, name='heat-add'),
    path('heat/<int:pk>/edit', views.heat_edit, name='heat-edit'),
    path('heat/<int:pk>/remove', views.heat_remove, name='heat-remove'),

    # CERTIFICATE
    path('certificate/all', views.certificate_index, name='certificate-main'),
    path('certificate/list', views.certificate_list, name='certificate-list'),
    path('certificate/add', views.certificate_add, name='certificate-add'),
    path('certificate/<int:pk>/edit', views.certificate_edit, name='certificate-edit'),
    path('certificate/<int:pk>/remove', views.certificate_remove, name='certificate-remove'),

    # SUPPLY
    path('supply/all', views.supply_index, name='supply-main'),
    path('supply/list', views.supply_list, name='supply-list'),
    path('supply/add', views.supply_add, name='supply-add'),
    path('supply/<int:pk>/edit', views.supply_edit, name='supply-edit'),
    path('supply/<int:pk>/remove', views.supply_remove, name='supply-remove'),

]
