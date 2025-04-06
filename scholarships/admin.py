from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django import forms
from django.contrib import messages
from django.http import HttpResponseRedirect
from .models import Scholarship
import pandas as pd

class CsvImportForm(forms.Form):
    csv_file = forms.FileField()

@admin.register(Scholarship)
class ScholarshipAdmin(admin.ModelAdmin):
    change_list_template = "admin/scholarship_changelist.html"
    
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('import-csv/', self.import_csv),
        ]
        return my_urls + urls

    def import_csv(self, request):
        if request.method == "POST":
            csv_file = request.FILES["csv_file"]
            df = pd.read_csv(csv_file)
            
            for index, row in df.iterrows():
                Scholarship.objects.update_or_create(
                    title=row['title'],
                    defaults={
                        'description': row['description'],
                        'eligibility': row['eligibility'],
                        'deadline': row['deadline'],
                        'amount': row['amount'],
                        'application_link': row['application_link']
                    }
                )
            self.message_user(request, "CSV imported successfully")
            return HttpResponseRedirect("..")
        
        form = CsvImportForm()
        payload = {"form": form}
        return render(request, "admin/csv_form.html", payload)
