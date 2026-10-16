
from . import views
from django.urls import path

urlpatterns = [
    path('',views.lista_citas, name='lista'),
    path('nuevo/', views.crear_cita, name='crear'),
    path('editar/<int:id>',views.editar_cita, name='editar'),
    path('eliminar/<int:id>',views.eliminar_cita, name='eliminar'),

]