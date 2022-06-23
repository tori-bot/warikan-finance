
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('profile_form/<int:id>',views.profile_form,name='profile_form'),

    path('account_form/<int:id>',views.account_form,name='account_form'),
    path('bill_form/<int:id>',views.bill_form,name='bill_form'),

    path('about/',views.about,name='about'),
    path('news/',views.news,name='news'),

]