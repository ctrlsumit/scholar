import django_filters
from .models import Scholarship

class ScholarshipFilter(django_filters.FilterSet):
    MIN_AMOUNT = 500
    MAX_AMOUNT = 50000
    
    amount__gte = django_filters.NumberFilter(
        field_name='amount', lookup_expr='gte',
        label='Minimum Amount',
        help_text=f'Enter amount ≥ {MIN_AMOUNT}'
    )
    
    amount__lte = django_filters.NumberFilter(
        field_name='amount', lookup_expr='lte', 
        label='Maximum Amount',
        help_text=f'Enter amount ≤ {MAX_AMOUNT}'
    )

    class Meta:
        model = Scholarship
        fields = {
            'eligibility': ['exact'],
            'deadline': ['gte', 'lte'],
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.filters['eligibility'].extra.update(
            {'empty_label': 'Select Eligibility Type'}
        )
