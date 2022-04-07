import imp
from rest_framework import viewsets
from rest_framework.response import Response
from customercare.models import Comment, Feedback
from customercare.serializers import CommentSerializer, FeedbackSerializer


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class FeedbackViewSet(viewsets.ModelViewSet):
    queryset = Feedback.objects.all()
    serializer_class = FeedbackSerializer
