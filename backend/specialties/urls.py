from django.urls import path
from . import views

urlpatterns = [
    path('', views.specialties, name='Specialties List'),
    path('<int:question_id>/', views.show, name='show'),
    path('<int:question_id>/create', views.create, name='store'),
    path('<int:question_id>/update', views.update, name='update'),
    path('<int:question_id>/delete', views.delete, name='delete'),
]