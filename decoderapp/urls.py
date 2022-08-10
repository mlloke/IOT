from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('decoder/', views.decoder_list.as_view()),
    path('decoder/<int:pk>/', views.decoder_detail.as_view()),

]

urlpatterns = format_suffix_patterns(urlpatterns)
