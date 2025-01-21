from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render
from django.core.cache import cache
import logging
from .models import TriviaQuestion

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
    
    template = loader.get_template("triviabackend/question_hidden_answer.html")

    context = {
        "question": question
    }

    return HttpResponse(template.render(context, request))

def alt_question(request, question_id):


    question = get_object_or_404(TriviaQuestion, pk=question_id)

    return render(request, "triviabackend/question_hidden_answer.html", {"question":question})