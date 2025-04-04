from django.urls import path
from .views import user_list, user_create, user_update, user_delete

urlpatterns = [
    path('', user_list, name='user_list'),
    path('create/', user_create, name='user_create'),
    path('update/<int:user_id>/', user_update, name='user_update'),
    path('delete/<int:user_id>/', user_delete, name='user_delete'),
]
