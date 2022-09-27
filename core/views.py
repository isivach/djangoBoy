from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from core.models import Author

class IndexView(TemplateView):
    template_name = "index.html"

class CreatAuthorView(CreateView):
    template_name = "create_author.html"
    model = Author
    fields = '__all__'
    success_url = '/'

class UpdateAuthorView(UpdateView):
    template_name = "create_author.html"
    model = Author
    fields = '__all__'
    success_url = '/'