from django.urls import path
from userapp import views
urlpatterns=[
    path('home/',views.home,name="home"),
    path('category/<dogg>', views.dog, name="dog"),
    path('cat/<catt>', views.cat, name="cat"),
    path('contact/', views.contact, name="contact"),
    path('savecontact/', views.savecontact, name="savecontact"),
    path('details/<int:dataid>/', views.details, name="dogs"),
    path('service/', views.service, name="service"),
    path('appoinment/', views.appoinment, name="appoinment"),
    path('saveappoinment/', views.saveappoinment, name="saveappoinment"),
    path('about/', views.about, name="about"),
    path('register/',views.register,name="register"),
    path('saveregister/',views.saveregister,name="saveregister"),
    path('login/',views.login,name='login'),
    path('userlogin/', views.userlogin, name='userlogin'),
    path('logout/', views.logout, name='logout'),
    path('request/', views.request, name="request"),
    path('saverequest/', views.saverequest, name="saverequest"),

]