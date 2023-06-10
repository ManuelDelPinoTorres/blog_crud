from django.urls import path

# importantisimo el .
from .views import BlogListView

app_name="blog"

urlpatterns = [
    path('',BlogListView.as_view(),name="home")
]
