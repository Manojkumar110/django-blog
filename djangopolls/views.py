from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from djangopolls.models import Question, Choice
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from django.views import generic

# Create your views here.

def detail(request, slug):
    try:
        question = Question.objects.get(slug=slug)
    except Question.DoesNotExist:
        raise Http404(' Question Does Not exist')
    question = get_object_or_404(Question, slug=slug)
    return render(request, "polls/detail.html", {'question':question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
        print('post method :', request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "polls/detail.html", {
            "question": question, 
            "error_message": "You didn't select a choice.",})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
   
def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/results.html", {"question": question})

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        return Question.objects.order_by("-pub_date")[:5]

# class DetailView(generic.DetailView):
#     model = Question
#     template_name = "polls/detail.html"

#     def get_queryset(self):
#         return Question.objects.filter(pub_date__lte=timezone.now())
