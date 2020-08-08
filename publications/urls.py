from django.urls import path

from . import views

app_name = 'publications'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('<int:pub_id>/', views.detail, name = 'detail'),
    path('<int:pub_id>/leave_comment/', views.leave_comment, name = 'leave_comment'),
    path('create_publication/', views.create_publication, name = 'create_publication'),
    path('perform_search/', views.perform_search, name = 'perform_search'),
]
