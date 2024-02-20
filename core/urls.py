from django.urls import path
from .views import HomePageView,SamplePageView

# Urls para las vistas basadas en clases.
urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('sample/', SamplePageView.as_view(), name="sample"),
]