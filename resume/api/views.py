from django.conf import settings
from rest_framework import viewsets

from resume.api.permissions import IsOwnerOrReadOnly
from resume.api.serializers import ResumeSerializer
from resume.models import Resume


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = (*settings.REST_FRAMEWORK['DEFAULT_PERMISSION_CLASSES'], IsOwnerOrReadOnly)
