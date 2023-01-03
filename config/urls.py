from django.contrib import admin
from django.urls import path, include

import warehouse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('warehouse.urls'))
]
