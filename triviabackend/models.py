from django.db import models
from django.contrib.postgres.fields import DateTimeRangeField

import json

class TriviaQuestion(models.Model):
    question_text = models.CharField(max_length=500)
    answer_text = models.CharField(max_length=500)
    valid_range = DateTimeRangeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return json.dumps({"question": self.question_text, "answer": self.answer_text}, indent=4)

class TriviaTopic(models.Model):
    name = models.CharField(max_length=200)

class TriviaQuestionTopics(models.Model):
    question = models.ForeignKey(TriviaQuestion, on_delete=models.RESTRICT)
    topic = models.ForeignKey(TriviaTopic, on_delete=models.RESTRICT)

class TriviaSubject(models.Model):
    name = models.CharField(max_length=200)

# many to many
class TriviaQuestionSubjects(models.Model):
    question = models.ForeignKey(TriviaQuestion, on_delete=models.RESTRICT)
    subject = models.ForeignKey(TriviaSubject, on_delete=models.RESTRICT)

class TriviaConditions(models.Model):
    name = models.CharField(max_length=200)

# e.g happened on this date, relationship to
class TriviaQuestionConditions(models.Model):
    question = models.ForeignKey(TriviaQuestion, on_delete=models.RESTRICT)
    condition = models.ForeignKey(TriviaSubject, on_delete=models.RESTRICT)


