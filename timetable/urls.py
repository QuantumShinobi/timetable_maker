from django.urls import path
from .views import *

app_name = "timetable"
urlpatterns = [
    path("", MainView.as_view(), name="home"),
    path("main_form", InputView.as_view(), name="main_form"),
    path("timetable", TimetableView.as_view(), name="show_timetable"),
    path("teacher_form", TeacherInput.as_view(), name="teacher_form"),
    path("clear_cookie", clear_cookie, name="clear_cookie"),

]
