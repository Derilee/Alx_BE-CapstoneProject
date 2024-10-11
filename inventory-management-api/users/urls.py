from .views import RegisterView, ProfileView, LoginView, LogoutView
from django.urls import path

#an endpoint that links a url to a view
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout')
]