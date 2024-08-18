from rest_framework.routers import DefaultRouter
from django.urls import path, include
from author.views import AuthorViewSet

router = DefaultRouter()
router.register(r'manage', AuthorViewSet, basename='manage')

urlpatterns = [
    path('', include(router.urls)),
]

app_name = "author"
