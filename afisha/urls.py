from django.contrib import admin
from django.urls import path
from movie_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/directors/', views.director_list_api_view),
    path('api/directors/<int:id>/', views.director_detail_api_view),
    path('api/movies/', views.movie_list_api_view),
    path('api/movies/<int:id>/', views.movie_detail_api_view),
    path('api/reviews/', views.review_list_api_view),
    path('api/reviews/<int:id>/', views.review_detail_api_view),
    path('api/movies/reviews/', views.movie_review_api_view)
]
