from django.urls import path, include
from rest_framework import routers

from resume.api.views import ResumeViewSet

router = routers.DefaultRouter()


router.register(r'', ResumeViewSet, basename='resume')

urlpatterns = [
    path('', include(router.urls)),
]
