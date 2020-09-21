 # -*- coding: utf-8 -*-

from django.urls import path
from . import views
urlpatterns=[
           path('',views.HomePageView.as_view(), name="home"),
           path('/<int:search_term>', views.HomePageView.as_view(), name="home"),
           path('spage1/<int:pk>',views.spage1View.as_view(),name = 'spage1'),
           path('search/',views.search,name="search"),
           path(r'create/',views.CreateStudent,name = "create"),
           path('success/<int:pk>',views.success.as_view(),name = "success"),
        #path('update/<slug:search_term>',views.UpdateStudent.as_view(),name = "update"),
           path('update/<int:pk>',views.UpdateStudent.as_view(),name = "update"),
           path('signup/',views.SignUpView.as_view(),name = "signup"),
            path('student/delete/<int:pk>',views.DeleteStudent.as_view(),name = "delete"),
           ]
