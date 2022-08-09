from django.urls import path

from . import views

urlpatterns = [
    path('decoder/', views.decoder_list),
    path('decoder/<int:pk>/', views.decoder_detail)

]
