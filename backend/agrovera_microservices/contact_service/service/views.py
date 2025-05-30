# views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
from service.serializers import ContactSerializer
from django.conf import settings

class ContactCreateView(APIView):
    def post(self, request):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            contact = serializer.save()

            send_mail(
                subject=f"Nouveau message de {contact.name}",
                message=f"Email: {contact.email}\n\nMessage:\n{contact.message}",
                from_email=settings.DEFAULT_FROM_EMAIL,
                recipient_list=["agroveratn@gmail.com"],  # doit être celui vérifié sur Elastic Email
                fail_silently=False
            )

            return Response({"message": "Message envoyé avec succès"}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
