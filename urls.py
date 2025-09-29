from django.urls import path
from .  import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('bankregister/',views.bankregister,name='bankregister'),
    path('userregister/',views.userregister,name='userregister'),
    # path('banklogin/',views.banklogin,name='banklogin'),
    # path('userlogin/',views.userlogin,name='userlogin'),

]