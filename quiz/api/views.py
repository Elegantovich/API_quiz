from asyncio.windows_events import NULL
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from .models import Question
from .serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
from .constant import URL, MESSAGE
import requests


class APIRequestQuestion(APIView):
    def post(self, request):
        try:
            questions_num = request.data['questions_num']
        except KeyError:
            response = {'response': MESSAGE}
            return Response(response, status=status.HTTP_404_NOT_FOUND)
        questions_num = request.data.get('questions_num')
        for _ in range(questions_num):
            response = requests.get(URL)
            ID_question = response.json()[0].get('id')
            response_text = response.json()[0].get('answer')
            question_text = response.json()[0].get('question')
            date_request = response.json()[0].get('created_at')
            data = {'ID_question': ID_question,
                    'response_text': response_text,
                    'question_text': question_text,
                    'date_request': date_request}
            serializer = QuestionSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(ID_question, response_text, question_text, date_request)
        previous_item_id = Question.objects.last().id - 1
        if not Question.objects.filter(id=previous_item_id).exists():
            response = {'question_text': None}
            return Response(response, status=status.HTTP_200_OK)
        last_obj = get_object_or_404(Question, id=previous_item_id)
        response = {'question_text': last_obj.question_text}
        return Response(response, status=status.HTTP_200_OK)
