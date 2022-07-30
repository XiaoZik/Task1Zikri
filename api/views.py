from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Notes
from .serializers import NotesSerializer
from rest_framework.decorators import action
from rest_framework.response import Response

@api_view(['GET'])
def getNotes(request):
    #To query the data
    items = Notes.objects.all()
    #Serializing the data and specifying that we want to query all data
    serializer = NotesSerializer(items, many = True)
    #Returning the data
    return Response(serializer.data)

@api_view(['POST'])
def addNotes(request): 
    serializer = NotesSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateNotes(request, pk): 
    note = Notes.objects.get(id = pk)
    serializer = NotesSerializer(instance = note, data = request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteNotes(request, pk): 
    note = Notes.objects.get(id = pk)
    note.delete()
    return Response('Note deleted')


