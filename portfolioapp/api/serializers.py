from rest_framework.serializers import ModelSerializer

from portfolioapp.models import Project, Contact


class ProjectSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ['name', 'description', 'thumbnail', 'link']


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = ['name', 'link', 'url']
