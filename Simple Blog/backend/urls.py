from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('blogs/', include('blogs.urls')),
    path('', views.index, name='home'),
    path('admin/', admin.site.urls),
]
