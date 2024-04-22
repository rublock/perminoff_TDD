from django.views.generic import ListView

from .forms import AddBookForm
from .models import Catalog


class ВookCreateView(ListView):
    """
    Представление: создание материалов на сайте
    """
    model = Catalog
    template_name = 'main.html'
    context_object_name = 'books'
    queryset = Catalog.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Моя библиотека'
        context['add_book_form'] = AddBookForm
        return context
