from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView
from .models import Note

class NoteCreateView(CreateAPIView):
    queryset = Note.objects.filter(is_active = True)
    # serializer_class = 
    

class NoteDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.filter(is_active = True)
    
    
    
    def perform_destroy(self, instance:Note):
        instance.is_active = False
        instance.save()
        
        