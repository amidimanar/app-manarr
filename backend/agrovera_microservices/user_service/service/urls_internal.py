from django.urls import path
from .views import MemberListCreateView, MemberRetrieveUpdateDestroyView

urlpatterns = [
    path('members/', MemberListCreateView.as_view()),
    path('members/<int:pk>/', MemberRetrieveUpdateDestroyView.as_view()),
]
