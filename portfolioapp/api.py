from rest_framework import viewsets
from .models import Project
from portfolioapp.api.serializers import ProjectSerializer
from rest_framework.permissions import AllowAny


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [AllowAny]