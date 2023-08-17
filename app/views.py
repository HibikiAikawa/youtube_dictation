from django.shortcuts import render
from .models import Question
from .forms import TextAreaForm


def index(request):
    return render(request, "index.html")


def get_question(request):
    question = Question.objects.order_by('?').first()
    form = TextAreaForm()
    return render(request, "question/question.html", {"question": question, "form": form})


def check_sentence(request, youtube_id, start_time):
    question = Question.objects.get(youtube_id=youtube_id, start_time=start_time)
    text = request.POST.get('textarea')
    print(question.sentence, type(question.sentence))
    print(text, type(text))
    if question.sentence == text:
        message = '正解！'
    else:
        message = '不正解！'

    return render(request, 'check.html', {"question": question, "message": message})
