from django.urls import path

from goals.views.board import BoardCreateView, BoardListView, BoardView
from goals.views.goal import GoalCreateView, GoalListView, GoalView

urlpatterns = [
    path("goal/create", GoalCreateView.as_view()),
    path("goal/list", GoalListView.as_view()),
    path("goal/<pk>", GoalView.as_view()),
    path("board/create", BoardCreateView.as_view()),
    path("board/list", BoardListView.as_view()),
    path("board/<pk>", BoardView.as_view()),
]
