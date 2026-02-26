from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    # Owner is read-only so users can't assign tasks to someone else
    owner = serializers.ReadOnlyField(source="owner.username")

    class Meta:
        model = Task
        fields = [
            "id",
            "title",
            "description",
            "is_completed",
            "priority",
            "due_date",
            "created_at",
            "updated_at",
            "owner",
        ]
