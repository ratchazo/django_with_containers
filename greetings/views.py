from django.views import generic
from .models import Greeting

class IndexView(generic.ListView):
    template_name = 'greetings/index.html'
    context_object_name = 'greeting_list'

    def get_queryset(self):
        """Return the all greetings."""
        return Greeting.objects.all()
