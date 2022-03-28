<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()),
]
=======
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index ),
]
>>>>>>> origin/changrae
