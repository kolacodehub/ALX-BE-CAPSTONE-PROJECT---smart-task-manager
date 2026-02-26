# Motivation imports
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

# Others sha
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # This override the default queryset so users ONLY see their own tasks
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(
            owner=self.request.user
        )  # Automatically set the owner to the user making the request


class MotivationView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        url = "https://zenquotes.io/api/random"

        try:
            # Make the request to ZenQuotes API with a strict 5-second timeout
            response = requests.get(url, timeout=5)
            response.raise_for_status()  # Triggers an error if the status code is 4xx or 5xx

            # ZenQuotes will returns an array contaning one dictionary
            data = response.json()
            quote = data[0].get("q")
            author = data[0].get("a")

            return Response({"quote": quote, "author": author}, status=200)

        except requests.exceptions.RequestException:
            # Fallback if the ext. API fails, times out, or user got have no network
            return Response(
                {
                    "quote": "Discipline is the bridge between goals and accomplishment.",
                    "author": "Jim Rohn",
                    "note": "External API unavailable, serving fallback quote.",
                },
                status=200,
            )
