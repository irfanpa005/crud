from django.urls import path
from .import views


urlpatterns=[
    path('',views.register,name='main'),
    path('index',views.index,name='index'),
    path('save_data/',views.save_data, name="saveData"),
    path('update/<int:data_id>',views.update, name="update"),
    path('delete/<int:data_id>',views.delete, name="delete"),
    path('login/',views.login,name='login')
]

