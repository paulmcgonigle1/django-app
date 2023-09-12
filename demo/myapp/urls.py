from django.urls import path
from . import views
from .views import Process, ReturnDummy

urlpatterns = [
    path("", views.home, name="home"),
    path("todos/", views.todos, name="Todos"),
    path("process/", Process.as_view, name="process_pdfs"),
    path("returndummy/", ReturnDummy.as_view(), name="returndummy"),
]
