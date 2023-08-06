from django.urls import path
from . import views #Se importa desde nuestra starapp << para escribir el path <<<<<<<<<<<<<<<<

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('task/', views.tasks, name='task'),
    path('logout/', views.signout, name='logout'),
    path('signin/', views.signin, name='signin'),
    path('task/create', views.create_task, name='create_task'),
    path('task/<int:task_id>', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/complete', views.task_complete, name='task_complete'),
    path('task/<int:task_id>/delete', views.task_delete, name='task_delete'),
    path('task_completed/', views.task_completed, name='task_completed'),
    
]
