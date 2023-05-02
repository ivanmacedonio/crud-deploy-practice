from .models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):

    queryset= Project.objects.all()
#En queryset indicamos que data va a manejar la view o endpoint
    
    permission_classes = [permissions.AllowAny]
#En permission_classes indicamos quienes tienen permisos para realizar operaciones 

    serializer_class = ProjectSerializer
#Indicamos quien va a serializar a JSON la data de la query 

