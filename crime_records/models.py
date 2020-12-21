from django.db import models

# Create your models here.

class CrimeRecord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    passport = models.ImageField(upload_to='offenders_images/', blank=True, null=True)
    date_of_birth = models.DateField()
    state_of_origin = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40, default='Nigeria')
    BVN = models.CharField(max_length=10)
    description = models.TextField()
    extra_note = models.CharField(max_length=300)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.created})'
