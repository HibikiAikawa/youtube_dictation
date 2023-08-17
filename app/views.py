from django.shortcuts import render

from youtube_transcript_api import YouTubeTranscriptApi
import numpy as np

from .models import Question
from .forms import TextAreaForm


def index(request):
    return render(request, "index.html")


def get_question(request):
    question = Question.objects.order_by('?').first()
    transcript = YouTubeTranscriptApi.list_transcripts(question.youtube_id)
    transcript_list = next(iter(transcript)).fetch()

    def get_random_idx(_transcript_list):
        idx = np.random.randint(1, len(_transcript_list)-2)
        start_time = transcript_list[idx]['start']
        pre_sentence = transcript_list[idx]['text']
        sentence = transcript_list[idx+1]['text']
        post_sentence = transcript_list[idx+2]['text']
        return start_time, pre_sentence, sentence, post_sentence, idx

    def pick_question(_transcript_list):
        start_time, pre_sentence, sentence, post_sentence, idx = get_random_idx(_transcript_list)
        if '[' in pre_sentence + sentence + post_sentence:
            pick_question()
        return start_time, pre_sentence, sentence, post_sentence, idx

    start_time, pre_sentence, sentence, post_sentence, idx = pick_question(transcript_list)
    question.start_time = int(start_time)
    question.pre_sentence = pre_sentence
    question.sentence = sentence
    question.post_sentence = post_sentence
    question.idx = idx

    form = TextAreaForm()
    return render(request, "question/question.html", {"question": question, "form": form})


def check_sentence(request, youtube_id, idx):
    question = Question.objects.get(youtube_id=youtube_id)
    transcript = YouTubeTranscriptApi.list_transcripts(youtube_id)
    transcript_list = next(iter(transcript)).fetch()
    text = request.POST.get('textarea')

    start_time = transcript_list[idx]['start']
    pre_sentence = transcript_list[idx]['text']
    sentence = transcript_list[idx+1]['text']
    post_sentence = transcript_list[idx+2]['text']

    question.start_time = int(start_time)
    question.pre_sentence = pre_sentence
    question.sentence = sentence
    question.post_sentence = post_sentence

    if question.sentence == text:
        message = '正解！'
    else:
        message = '不正解！'

    return render(request, 'check.html', {"question": question, "message": message})
