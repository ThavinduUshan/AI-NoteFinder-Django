from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Note, Category
from .serializers import NoteSerializer, CategorySerializer
from .utils import ChromaDB


@api_view(['GET', 'POST'])
def note_list(request):
    if request.method == 'GET':
        notes = Note.objects.select_related('category').all()
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            note = serializer.save()
            collection = ChromaDB.get_or_create_collection()
            collection.add(documents=[note.content], metadatas=[
                {"title": note.title, "category": note.category}], ids=[str(note.id)])
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search_notes(request):
    query = request.query_params.get('query', '')
    if not query:
        return Response({"error": "Search value can't be empty"}, status=status.HTTP_400_BAD_REQUEST)
    try:
        collection = ChromaDB.get_collection()
        results = collection.query(
            query_texts=[query], n_results=6, include=["documents"])
        return Response(results, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'POST'])
def category_list(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
