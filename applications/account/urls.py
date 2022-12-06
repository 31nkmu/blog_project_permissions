from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from applications.account import views

urlpatterns = [
    path('register/', views.RegisterApiView.as_view()),
    path('login/', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
]
