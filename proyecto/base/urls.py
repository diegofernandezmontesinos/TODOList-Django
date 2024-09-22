from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea, EliminarTarea, Login, logout_view, PaginaRegistro

urlpatterns = [
               path('', ListaPendientes.as_view(), name='tareas'),
               path('login/', Login.as_view(), name='login'),
               path('logout/', logout_view, name='logout'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editar-tarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('eliminar-tarea/<int:pk>', EliminarTarea.as_view(), name='eliminar-tarea')
               ]
