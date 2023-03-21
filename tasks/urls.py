from django.urls import path
from tasks import views
urlpatterns = [
    path('', views.index, name='index'),
    path('update/<int:pk>', views.update, name='update'),
    path('delete/<int:pk>', views.delete, name='delete'),
]
