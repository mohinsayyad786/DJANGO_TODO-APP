from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('home',views.home),
    path('product',views.product),
    path('contact',views.contact),
    path('edit/<rid>',views.edit),
    path('delete/<rid>',views.delete),
    path('evenodd/<n>',views.evenodd),
    path('tloop',views.loop),
    path('',views.index),
    path('about',views.about),
    path('create',views.create_task),
    path('course',views.cdashboard),
    path('all',views.cdashboard),
    path('ltoh',views.lowtohigh),
    path('htol',views.hightolow),
    path('ltoh',views.asending),
    path('htol',views.desending),
    path('dform',views.showform),
    path('modelform',views.showmodelform),
    path('cview',views.MyView.as_view()),
    path('register',views.register),
    path('login',views.user_login),
    path('logout',views.user_logout),
    path('set',views.setcookie),
    path('get',views.getcookie),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('delsession',views.del_session),
    path('getid',views.getloggeduserid),

    

]