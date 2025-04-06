from django.views.generic import ListView
from django.core.paginator import Paginator
from .models import Scholarship
from .filters import ScholarshipFilter

class ScholarshipListView(ListView):
    model = Scholarship
    template_name = 'scholarships/list.html'
    context_object_name = 'scholarships'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        self.filterset = ScholarshipFilter(
            self.request.GET, queryset=qs
        )
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = self.filterset
        paginator = Paginator(self.object_list, self.paginate_by)
        page_number = self.request.GET.get('page')
        context['page_obj'] = paginator.get_page(page_number)
        return context
