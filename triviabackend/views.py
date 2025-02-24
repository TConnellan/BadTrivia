from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.core.cache import cache
import logging
from .models import TriviaQuestion
from collections import defaultdict
from random import randrange

logger = logging.Logger(__name__)

def index(request):
    return HttpResponse("This is a trivia site")

def question(request, question_id):

    question = cache.get(question_id, None)
    if question is None:
        logger.info(f"Question #{question_id} was not cached")

        try:
            question = TriviaQuestion.objects.get(pk=int(question_id))
        except TriviaQuestion.DoesNotExist:
            question = None
    
        if question:
            cache.set(question_id, question)

    if not request.session.get("stats"):
        request.session["stats"] = defaultdict(int)

    request.session.get("stats")["attempted"] += 1

    attempted = request.session.get("stats").get("attempted")
    successful = request.session.get("stats").get("successful", 0)

    if not request.session.get("history"):
        request.session["history"] = {
            "ids": TriviaQuestion.objects.values_list('id', flat=True)
        }
        request.session["history"]["range"] = [0, len(request.session["history"]["ids"]) - 1]
    
    template = loader.get_template("triviabackend/question_hidden_answer.html")

    context = {
        "question": question,
        ""
        "stats": {
            "attempted": attempted,
            "successful": successful
        }
    }

    return HttpResponse(template.render(context, request))


def random_question(request):

    if not request.session.get("stats"):
        request.session["stats"] = defaultdict(int)

    request.session.get("stats")["attempted"] += 1

    attempted = request.session.get("stats").get("attempted")
    successful = request.session.get("stats").get("successful", 0)

    if not request.session.get("history"):
        request.session["history"] = {
            "ids": list(TriviaQuestion.objects.values_list('id', flat=True))
        }
        request.session["history"]["range"] = [0, len(request.session["history"]["ids"]) - 1]

    ids = request.session["history"]["ids"]
    start, end = request.session["history"]["range"]
    print(start, end, len(ids))
    
    template = loader.get_template("triviabackend/question_hidden_answer.html")

    idx = randrange(start, end + 1)
    question_id = ids[idx]

    question = cache.get(question_id, None)
    if question is None:
        logger.info(f"Question #{question_id} was not cached")

        try:
            question = TriviaQuestion.objects.get(pk=int(question_id))
        except TriviaQuestion.DoesNotExist:
            question = None
    
        if question:
            cache.set(question_id, question)

    ids[idx], ids[end] = ids[end], ids[idx]
    request.session["history"]["range"][1] = end - 1

    context = {
        "question": question,
        ""
        "stats": {
            "attempted": attempted,
            "successful": successful
        }
    }

    return HttpResponse(template.render(context, request))

