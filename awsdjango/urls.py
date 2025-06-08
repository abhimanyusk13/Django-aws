from django.contrib import admin
from django.urls import path
from core.views import home


def health(request):
    """Simple health check view."""
    from django.http import HttpResponse
    return HttpResponse("ok")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('health/', health, name='health'),
]
