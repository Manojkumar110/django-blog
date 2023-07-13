from django.urls import path
from djangopolls.views import  results, vote, IndexView, detail
# DetailView


app_name = "polls"
urlpatterns = [
    path("index/", IndexView.as_view(), name="index"),
    # path("<int:pk>/", DetailView.as_view(), name="detail"),
    path("<str:slug>/", detail, name="detail"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("<int:question_id>/results/", results, name="results"),
]
