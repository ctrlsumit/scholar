from django.db import models
from django.core.validators import MinValueValidator

class Scholarship(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    eligibility = models.CharField(max_length=100, 
        choices=[('merit', 'Merit-Based'), ('need', 'Need-Based')])
    deadline = models.DateField()
    amount = models.DecimalField(max_digits=10, decimal_places=2,
        validators=[MinValueValidator(0)])
    application_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['deadline']),
            models.Index(fields=['amount']),
        ]
        ordering = ['-deadline']

    def __str__(self):
        return self.title
