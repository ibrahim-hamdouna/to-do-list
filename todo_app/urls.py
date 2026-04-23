from django.urls import path
from . import views

urlpatterns = [
    # Entry point of the app (Login)
    path('', views.LoginView.as_view(), name='login'),
    # User Registration
    path('signup/', views.SignupView.as_view(), name='signup'), 
    # To Do List Tasks Management
    path('tasks/', views.TasksView.as_view(), name='tasks'),
    # Action: Toggle task completion status (Requires task ID)
    path('tasks/complete/<int:id>/', views.TasksView.as_view(), name='complete_task'),
    # Action: Update task description (Requires task ID)
    path('tasks/update/<int:id>/', views.TasksView.as_view(), name='update_task'),
    # Action: Delete task (Requires task ID)
    path('tasks/delete/<int:id>/', views.TasksView.as_view(), name='delete_task'),
]