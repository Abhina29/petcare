from django.urls import path
from adminapp import views
urlpatterns=[
    path('index/',views.index,name="index"),
    path('add_pets/', views.add_pets, name="add_pets"),
    path('savepets/', views.savepets, name="savepets"),
    path('display_pets/', views.display_pets, name="display_pets"),
    path('delpets/<int:id>/', views.delpets, name="delpets"),
    path('editpets/<int:id>/', views.editpets, name="editpets"),
    path('update/<int:id>/', views.update, name="update"),
    path('logg/', views.logg, name="logg"),
    path('log/', views.log, name="log"),
    path('logout_pg/', views.logout_pg, name="logout_pg"),
    path('category/', views.category, name="category"),
    path('savecategory/', views.savecategory, name="savecategory"),
    path('display_category/', views.display_category, name="display_category"),
    path('delcategory/<int:id>/', views.delcategory, name="delcategory"),
    path('addservice/', views.addservice, name="addservice"),
    path('saveservice/', views.saveservice, name="saveservice"),
    path('displayservice/', views.displayservice, name="displayservice"),
    path('editservice/<int:id>/', views.editservice, name="editservice"),
    path('updateservice/<int:id>/', views.updateservice, name="updateservice"),
    path('delservice/<int:id>/', views.delservice, name="delservice"),
    path('displayadopt/', views.displayadopt, name="displayadopt"),
    path('deladopt/<int:id>/', views.deladopt, name="deladopt"),
    path('saveaccept/<int:id>/', views.saveaccept, name="saveaccept"),

]