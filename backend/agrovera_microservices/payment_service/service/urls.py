from django.contrib import admin
from django.urls import path, include
from service.views import(
    MemberPaymentListCreateView,
    MemberPaymentRetrieveUpdateView
)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('service.urls_internal')),
    path('payments/', MemberPaymentListCreateView.as_view(), name='payment-list-create'),
    path('payments/<int:pk>/', MemberPaymentRetrieveUpdateView.as_view(), name='payment-detail')
 
]
