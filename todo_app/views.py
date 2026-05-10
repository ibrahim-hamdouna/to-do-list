from .serializers import TasksSerializer, LoginSerializer, UserSerializer
from django.shortcuts import render, redirect, get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import SessionAuthentication
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth import login
from django.contrib import messages
from rest_framework import status
from .models import Tasks

# Create your views here.

class TasksView(APIView):
    """
    Unified View for Task Management.
    Handles the dashboard display via GET and API-style mutations (POST, PATCH, DELETE).
    """

    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Tasks.objects.filter(user = request.user)

        # Convert queryset to JSON (DRF) so we can pass it to the HTML template
        serializer = TasksSerializer(tasks, many = True)

        # Pre-calculating stats here to avoid complex logic in the HTML template
        context = {
            'tasks': serializer.data,
            'user': request.user,
            'total_tasks': tasks.count(),
            'pending_tasks': tasks.filter(is_completed=False).count(),
            'completed_tasks': tasks.filter(is_completed=True).count()
        }

        return render(request, 'todo_app/tasks.html', context)
    
    def post(self, request):
        """
        Handle POST requests to create a new task.
        """

        # Initialize serializer with submitted form data
        serializer = TasksSerializer(data = request.data)

        if serializer.is_valid():

            # The user=request.user ensures the task is linked to the logged-in user.
            serializer.save(user=request.user) 
            return redirect('tasks')

        else:

            # Convert DRF serializer errors into Django UI messages
            for field, errors in serializer.errors.items():
                for error in errors:
                    if field == 'non_field_errors':
                        messages.error(request, error)
                        
                    else:
                        messages.error(request, f"{error}")

        return redirect('tasks')

    def patch(self, request, id):
        task = Tasks.objects.get(id=id)

        # If a description is provided, we update it; otherwise, we toggle completion
        if 'description' in request.data:
            task.description = request.data['description']

        else:
            task.is_completed = not task.is_completed

        task.save()
        return Response(status=status.HTTP_200_OK)

    def delete(self, request, id):
        Tasks.objects.get(id = id).delete() # Direct delete to save a line of code
        return Response(status=status.HTTP_204_NO_CONTENT)

@method_decorator(never_cache, name='dispatch')
class LoginView(APIView):
    """
    API View for handling user login.
    """
    def get(self, request):
        return render(request, 'todo_app/login.html')
    
    def post(self, request):
        # Initialize serializer with submitted form data
        serializer = LoginSerializer(data = request.data)

        if serializer.is_valid():

            # Get the authenticated user from the serializer
            user = serializer.validated_data['user']

            # Create a secure session and send a session cookie to the browser.
            # This makes the user "remembered" across different pages.
            login(request, user)    
            return redirect('tasks')

        else:

            # Convert DRF serializer errors into Django UI messages
            for field, errors in serializer.errors.items():
                for error in errors:
                    messages.error(request, f"{error}")

        # Re-render form with previously typed data so the user doesn't have to restart
        return render(request, 'todo_app/login.html', {'typed_data': request.data})

class SignupView(APIView):
    """
    Handles new user registration.
    Displays the signup form and processes account creation.
    """

    def get(self, request):
        return render(request, 'todo_app/signup.html')
    
    def post(self, request):
        # Initialize serializer with submitted form data
        serializer = UserSerializer(data = request.data)

        if serializer.is_valid():

            # Create user and hash password via the serializer's create() method
            serializer.save()
            return redirect('login')

        else:

            # Convert DRF serializer errors into Django UI messages
            for field, errors in serializer.errors.items():
                for error in errors:
                    if field == 'non_field_errors':
                        messages.error(request, error)

                    else:

                        # Format field names (e.g., 'first_name' becomes 'First Name')
                        field_name = field.replace('_', ' ').title()
                        messages.error(request, f"{field_name}: {error}")

        # Re-render form with previously typed data so the user doesn't have to restart
        return render(request, 'todo_app/signup.html', {'typed_data': request.data})