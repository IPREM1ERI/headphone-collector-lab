from django.urls import path
from . import views

urlpatterns = [
  path('', views.Home.as_view(), name='home'),
  path('about/', views.about, name='about'),
  path('headphones/', views.headphones_index, name='headphones_index'),
  path('headphones/<int:headphone_id>/', views.headphones_detail, name='headphones_detail'),
  path('headphones/create/', views.HeadphoneCreate.as_view(), name='headphones_create'),
  path('headphones/<int:pk>/update/', views.HeadphoneUpdate.as_view(), name='headphones_update'),
  path('headphones/<int:pk>/delete/', views.HeadphoneDelete.as_view(), name='headphones_delete'),
  path('headphones/<int:headphone_id>/add_listened/', views.add_listened, name='add_listened'),
  path('equipment/create/', views.EquipmentCreate.as_view(), name='equipment_create'),
  path('equipment/<int:pk>/', views.EquipmentDetail.as_view(), name='equipment_detail'),
  path('equipment/', views.EquipmentList.as_view(), name='equipment_index'),
  path('equipment/<int:pk>/update/', views.EquipmentUpdate.as_view(), name='equipment_update'),
  path('equipment/<int:pk>/delete/', views.EquipmentDelete.as_view(), name='equipment_delete'),
  path('headphone/<int:headphone_id>/assoc_equipment/<int:equipment_id>/', views.assoc_equipment, name='assoc_equipment'),
  path('accounts/signup/', views.signup, name='signup'),
]