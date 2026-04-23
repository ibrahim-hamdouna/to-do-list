from rest_framework.validators import UniqueValidator
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Tasks

class TasksSerializer(serializers.ModelSerializer):
    """
    Serializes a Tasks model instance into JSON format.
    Validates the data before saving it to the database.
    Contain custom validations for the task description.
    """
    class Meta:
        model = Tasks
        fields = ['id', 'description', 'is_completed', 'created_at', 'updated_at']

        extra_kwargs = {
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }
        validate = UniqueValidator(queryset=Tasks.objects.all(), message="Task with this description already exists.")    
    
    def validate(self, attrs):
        if not attrs.get('description'):
            raise serializers.ValidationError({'error': 'Task cannot be empty'})
        return attrs
    
    def validate_description(self, value):
        """
        Prevent the user from entering symbols or special characters in the task description
        """

        if any (not (char.isalnum() or char.isspace() or char in ['?', '-', '_']) for char in value):
            raise serializers.ValidationError('Task must contain only alphanumeric characters or numbers')
        return value

class UserSerializer(serializers.ModelSerializer):
    """
    Serializes a User model instance into JSON format.
    Validates the data before saving it to the database.
    Contain custom validations for the first name, last name and username.
    """

    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'username', 'password', 'email']

        # Extra arguments for the model fields
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'required': True, 'allow_blank': False},
            'last_name': {'required': True, 'allow_blank': False},
            'username': {'required': True, 'allow_blank': False},
            'email': {
                'required': True,
                'validators': [UniqueValidator(queryset=User.objects.all(), message="A user with that email already exists.")]
            }
        }
    
    def create(self, validated_data):
        """
        Override the create method to create a new user, handling the password hashing.
        """

        user = User.objects.create_user(**validated_data)
        return user
    
    def validate_first_name(self, value):
        """
        Prevent the user from entering non-alphabetic characters in the first name
        """

        if any (not char.isalpha() for char in value):
            raise serializers.ValidationError('First name must contain only alphabetic characters')
        return value
    
    def validate_last_name(self, value):
        """
        Prevent the user from entering non-alphabetic characters in the last name
        """

        if any (not char.isalpha() for char in value):
            raise serializers.ValidationError('Last name must contain only alphabetic characters')
        return value
    
    def validate_username(self, value):
        """
        Prevent the user from entering non-alphanumeric characters in the username
        """

        if any (not char.isalnum() for char in value):
            raise serializers.ValidationError('Username must contain only alphanumeric characters or numbers')
        return value
    
class LoginSerializer(serializers.Serializer):
    """
    Serializer for user authentication. 
    Does not map to a model; used solely to validate credentials.
    """

    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        """
        Object-level validation to verify if credentials match a valid user.
        """

        username = attrs.get('username')
        password = attrs.get('password')
        if username and password:

            # Django's authenticate() checks credentials against the database
            user = authenticate(username=username, password=password)

            if not user:
                raise serializers.ValidationError({'error': 'Username or password is incorrect'})

            # If user is found, add it to the attributes to use it later in the LoginView and pass username for the tasks page.
            attrs['user'] = user

        return attrs
