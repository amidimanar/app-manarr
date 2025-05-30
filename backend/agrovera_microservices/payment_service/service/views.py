from rest_framework import generics
from .models import MemberPayment
from .serializers import MemberPaymentSerializer


# CRUD Paiements
class MemberPaymentListCreateView(generics.ListCreateAPIView):
    queryset = MemberPayment.objects.all()
    serializer_class = MemberPaymentSerializer
    permission_classes = []

    def perform_create(self, serializer):
        name = self.request.data.get('name')
        phone=self.request.data.get('phone')
        payment_status = self.request.data.get('payment_status')
        payment_date = self.request.data.get('payment_date')

        serializer.save(name=name, phone=phone, payment_status=payment_status, payment_date=payment_date)

class MemberPaymentRetrieveUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = MemberPayment.objects.all()
    serializer_class = MemberPaymentSerializer
    permission_classes = []
