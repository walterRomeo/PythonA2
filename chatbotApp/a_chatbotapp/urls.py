from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
urlpatterns = [

   path('', views.faq, name='faq'),

]
urlpatterns = [
   path('', views.contact),
]