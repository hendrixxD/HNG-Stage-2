from .models import Person
from django.shortcuts import render
from .serializers import PersonSerializer
from rest_framework import generics, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


# Create your views here.
class PersonListCreateView(generics.ListCreateAPIView):
    """creates a new person object
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetailView(generics.RetrieveUpdateDestroyAPIView):
    """Fetch details of a person
        Updates details of a person
        Deletes a person
    """
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    lookup_url_kwarg = 'parameter'  # Use 'parameter' as the lookup URL keyword argument
    # lookup_field = 'id'
    # lookup_field = 'name'
    
    def get_object(self):
        parameter = self.kwargs.get('parameter')
        try:
            if isinstance(parameter, int):
                # Try to lookup by user_id (integer)
                return Person.objects.get(id=parameter)
            else:
                # Try to lookup by name (string)
                return Person.objects.get(name=parameter)
        except Person.DoesNotExist:
            return Response(
                {"message": "Person not found."},
                status=status.HTTP_404_NOT_FOUND
            )

