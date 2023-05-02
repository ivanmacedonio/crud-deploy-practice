from rest_framework import routers
from .api import ProjectViewSet

router= routers.DefaultRouter()
#defaultrouter se encarga de crear un CRUD automaticamente a la direccion 
#que asignemos dicho router 

router.register('api/projects', ProjectViewSet, 'projects')

#el conjunto de rutas se encuentra en la url de api/projects, donde 
#la viewset que dara la informacion es ProjectViewSet

urlpatterns = router.urls #las registramos en el archivo main de urls 

#..lo agregamos a urls.py (main) incluyendo el archivo entero, es decir, 
#le enviamos todas las urls del router a una misma direccion

