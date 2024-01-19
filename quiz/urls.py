# showQuiz
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.showCat, name="show_quizes"),
    path("user_history", views.result_history, name="result"),
    path(
        "delete_result_history",
        views.delete_result_history,
        name="delete_result_history",
    ),
    path("questions/<int:cat_id>/", views.cat_questions, name="questions"),
    path(
        "submit_answer/<int:cat_id>/<int:quest_id>",
        views.submit_form,
        name="submit_form",
    ),
]
