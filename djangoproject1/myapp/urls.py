from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepageview,name="home"),
     path('about',views.aboutpageview,name="about"),
      path('contect',views.contactpageview,name="contact"),
        path('form',views.myform,name="myform"),
          path('formprocess',views.process,name="process"),
            path('slist',views.studentlist.as_view(),name="s1"),  
]
