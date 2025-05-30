from django.urls import path
from .views import MemberPaymentListCreateView, MemberPaymentRetrieveUpdateView

urlpatterns = [
    path('payments/', MemberPaymentListCreateView.as_view()),
    path('payments/<int:pk>/', MemberPaymentRetrieveUpdateView.as_view()),
]
