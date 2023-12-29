from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *


router = DefaultRouter()
router.register(r'users', UsersViewSet)
router.register(r'gender', GenderViewSet)
router.register(r'roles', RolesViewSet)
router.register(r'depositories', DepositoriesViewSet)
router.register(r'semesters', SemestersViewSet)
router.register(r'cities', CitiesViewSet)
router.register(r'libraries', LibrariesViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationAPIView.as_view(), name='register'),
    path('login/', UserLoginAPIView.as_view(), name='login'),
    path('logout/', UserLogoutAPIView.as_view(), name='logout'),
]