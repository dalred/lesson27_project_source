# TODO настройте здесь urls для заданий сourses, new_courses, find_by_name, who's_author
from django.urls import path

from adverb import views
from adverb.views import AdvEntityView

urlpatterns = [
    path("", views.advertisements),
    path("<int:pk>/", AdvEntityView.as_view())
]
