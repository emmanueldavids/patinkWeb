from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index',views.index, name='index'),
    path('about', views.about, name='about'),
    path('portfolio', views.portfolio, name='portfolio'),
    path('contact', views.contact, name='contact'),
    path('services', views.services, name='services'),
    # path('add/', views.add_task, name='add_task'),
    # path('edit/<int:task_id>/', views.edit_task, name='edit_task'),
    # path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
]