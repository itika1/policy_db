from django.urls import path
from . import views


urlpatterns = [
    path('admin/admin/policies/policy/add/', views.get_policy_fields, name='get_policy_fields'),
    path('policies/', views.policy_list, name='policy_list'),
    path('new/', views.policy_create, name='policy_create'),
    path('<int:pk>/edit/', views.policy_update, name='policy_update'),
    path('<int:pk>/delete/', views.policy_delete, name='policy_delete'),
    path('get_policy_fields/', views.get_policy_fields, name='get_policy_fields'),

]
