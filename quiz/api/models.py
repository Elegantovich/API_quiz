from django.db import models


class Question(models.Model):
    id = models.AutoField(
        primary_key=True,
        verbose_name='Unique number'
    )
    ID_question = models.IntegerField(
        unique=True,
        verbose_name='ID of question',
        )
    question_text = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Text of question'
        )
    response_text = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Text of response'
        )
    date_request = models.CharField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Date of create question'
        )

    def __str__(self):
        return self.question_text
