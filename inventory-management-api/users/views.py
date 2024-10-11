from django.shortcuts import render
from .models import User, Profile
from .serializers import RegisterSerializer, LoginSerializer, ProfileSerializer
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import logout
from rest_framework_simplejwt.tokens import RefreshToken


#A register view that helps create a new user
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]


#profile view to retrieve and update the profile details
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAuthenticated]

    #gets and returns the profile of the current user
    def get_object(self):
        return self.request.user.profile


#login view to handle user login and token refresh for each session and returns a refresh token and an access token
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh),
                             'access': str(refresh.access_token)})
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)


#logout view to handle user logout and token refresh and blacklist
class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            refresh_token = request.data['refresh_token']
            token = RefreshToken(refresh_token)
            token.blacklist()
            logout(request)
            return Response({'detail': 'You have successfully logged out'}, status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)