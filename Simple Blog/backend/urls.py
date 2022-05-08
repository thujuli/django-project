from django.contrib import admin
from django.urls import path, include
from .views import HomeTemplateView

urlpatterns = [
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('', HomeTemplateView.as_view(), name='home'),
    path('admin/', admin.site.urls),
]
