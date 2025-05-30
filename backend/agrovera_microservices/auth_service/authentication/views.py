from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .serializers import LoginSerializer

class LoginAPI(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                return Response({"status": False, "error": "Invalid credentials"}, status=400)

            user = authenticate(username=user.username, password=password)
            if user and user.is_superuser:
                token, _ = Token.objects.get_or_create(user=user)
                return Response({
                    "status": True,
                    "data": {
                        "token": str(token)
                    }
                }, status=200)
            else:
                return Response({"status": False, "error": "Unauthorized: Not an admin"}, status=403)
        return Response({"status": False, "error": "Invalid credentials"}, status=400)
