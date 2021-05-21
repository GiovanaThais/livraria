from rest_framework import viewsets
from livros.api import serializers
from livros import models
from rest_framework.permissions import IsAuthenticated

class LivrosViewSets(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    
    serializer_class = serializers.LivrosSerializer
    queryset = models.Livros.objects.all()
    