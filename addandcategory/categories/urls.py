# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path

from categories import views
from categories.views import CategoryDetailView

urlpatterns = [
    path("", views.categories),
    path("<int:pk>/", CategoryDetailView.as_view()),
]
