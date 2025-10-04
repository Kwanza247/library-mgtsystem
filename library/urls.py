from django.urls import path, include
from .views import (
    UserViewSet,
    BookViewSet,
    TransactionViewSet,
    CategoryViewSet,
    register,
    login,
    logout,
)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'categories', CategoryViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

    #authentication
    path('api/register/', register, name='register'),
    path('api/login', login, name='login'),
    path('api/logout', logout, name='logout'),
]


