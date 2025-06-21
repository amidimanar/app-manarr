from django.contrib import admin
from django.urls import path, include
from authentication.views import LoginAPI  # ✅ ajoute ceci

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('login/', LoginAPI.as_view()),
    path('', include("django_prometheus.urls")),
]
