from django.urls import path
from articles import views



urlpatterns = [
    # user/
    path('', views.ArticleView.as_view()),
 
]