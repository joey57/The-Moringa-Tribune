from django.urls import path
from . import views

urlpatterns=[
  path('welcome/', views.welcome, name = 'welcome'),
  path('today/',views.news_of_day , name='newsToday')
]
 