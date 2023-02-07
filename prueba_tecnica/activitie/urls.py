from django.urls import path
from activitie.views import CreateActivity

urlpatterns = [
    path('createActivity/', CreateActivity.as_view())
]