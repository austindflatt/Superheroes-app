from . import views
from django.urls import path

app_name = 'Superhero'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:superhero_id>/', views.detail, name='detail'),
    path('new/', views.create, name='create_new_superhero'),
    path('edit/<int:superhero_id>/', views.edit, name='edit'),
    path('delete/<int:superhero_id>/', views.delete, name='delete')
]