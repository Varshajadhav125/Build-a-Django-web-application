from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('add.task',views.taskAdd,name = "taskadd"),
    path('update.task/<str:pk>/',views.taskUpdate,name = "taskupdate"),
    path('delete.task/<str:pk>/',views.taskdelete,name = "taskdelete")
]    