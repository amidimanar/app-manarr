from django.contrib import admin
from django.urls import path
from service.views import ContactCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]
