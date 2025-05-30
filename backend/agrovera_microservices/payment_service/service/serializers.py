from rest_framework import serializers
from .models import MemberPayment

class MemberPaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberPayment
        fields = '__all__'
