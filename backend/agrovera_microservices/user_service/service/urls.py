from django.contrib import admin
from django.urls import path, include
from service.views import (
    MemberListCreateView,
    ContactCreateView,
    MemberRetrieveUpdateDestroyView
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('service.urls_internal')),
    path('member/', MemberListCreateView.as_view(), name='member-list'),
    path('member/<int:pk>/', MemberRetrieveUpdateDestroyView.as_view(), name='member-detail'),
    path('contact/', ContactCreateView.as_view(), name='contact'),
]
