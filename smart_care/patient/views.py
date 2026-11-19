from django.shortcuts import render
from rest_framework import viewsets
from . import models
from .serializers import PatientSerializer
from rest_framework.views import APIView
from .serializers import PatientCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token


class PatientViewSet(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = PatientSerializer

class patientregisterapiview(APIView):
    serializer_class = PatientCreateSerializer

    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))   
            confirmation_link = f"http://127.0.0.1:8000/patients/activate/{uid}/{token}/"
            email_subject = 'Activate your account'
            email_body = render_to_string(
                "activation_email.html",
                {
                    "user": user,
                    "confirmation_link": confirmation_link,
                },
            )
            email = EmailMultiAlternatives( email_subject, '', to=[user.email] )
            email.attach_alternative(email_body, "text/html")
            email.send()
            return Response({"message": "User registered successfully. Please check your email to activate your account."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def activate_account(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = models.User.objects.get(pk=uid)
    except (models.User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, "register")
    else:
        return render(request, "register")

class UserloginAPIView(APIView):
    # serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = UserLoginSerializer(data=self.request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token, created = Token.objects.get_or_create(user=user)
                login(request, user)
                return Response({"token": token.key, "user_id": user.id})
            else:
                return Response({"error": "Invalid credentials."})
        return Response(serializer.errors) 

class UserlogoutAPIView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return Response({"message": "Logged out successfully."})