from django.urls import path
from djangopolls.views import  results, vote, detail, index
# DetailView
# IndexView

app_name = "polls"
urlpatterns = [
    path("index/", index, name="homepage"),
    path("<str:slug>/", detail, name="detail"),
    path("<int:question_id>/vote/", vote, name="vote"),
    path("<int:question_id>/results/", results, name="results"),
]
