from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, MotivationView

# The router automatically generates the GET, POST, PUT, PATCH, and DELETE routes
router = DefaultRouter()
router.register(r"", TaskViewSet, basename="task")

urlpatterns = [
    path("motivation/", MotivationView.as_view(), name="motivation"),
    path("", include(router.urls)),
]


# Take Note oo
"""
GET /api/tasks/ (List your tasks)
POST /api/tasks/ (Create a task)
GET /api/tasks/<id>/ (View a specific task)
PUT /api/tasks/<id>/ (Update a task)
DELETE /api/tasks/<id>/ (Delete a task)

And in postman, use:-
Bearer + access key
"""
