from django.shortcuts import render
from .models import Question


def index(request):
    return render(request, "index.html")


def get_solution(request):
    question = Question.objects.order_by('?').first()  # ランダムに一つのQuestionを取得
    return render(request, "index.html", {"question": question})


def check_sentence(request):
    # question = Question.objects.get(pk=question_id)
    # is_correct = None

    # if request.method == "POST":
    #     form = SentenceForm(request.POST)
    #     if form.is_valid():
    #         is_correct = form.cleaned_data['sentence'] == question.sentence
    # else:
    #     form = SentenceForm()

    # context = {
    #     'form': form,
    #     'question': question,
    #     'is_correct': is_correct,
    # }

    return render(request, 'index.html')
