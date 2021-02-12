from rest_framework import viewsets

from portfolioapp.models import Project, Contact
from .serializers import ProjectSerializer, ContactSerializer


class ProjectViewSet(viewsets.ModelViewSet):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()


class ContactViewSet(viewsets.ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
