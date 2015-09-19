from django.shortcuts import render
from django.shortcuts import get_object_or_404
from pastebin.models import Paste
from django.views import generic

display_info = {'queryset': Paste.objects.all()}
create_info = {'model': Paste}

class ObjectList(generic.ListView):
    allow_empty=True 
    template_name = 'pastebin/paste_list.html'
    def get_queryset(self):
        return Paste.objects.all()
    
class CreateObject(generic.CreateView):
    model = Paste
    template_name = 'pastebin/paste_form.html'
    fields = ['title', 'poster', 'syntax', 'content'] 
    
class ObjectDetail(generic.DetailView):
    template_name = 'pastebin/paste_detail.html'
    def get_object(self):
       return get_object_or_404(Paste, pk=self.kwargs['object_id'])
