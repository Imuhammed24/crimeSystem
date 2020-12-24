from django.db import models
from django.db.models import Q


SEX = (
    ('male', 'male'),
    ('female', 'female'),
    ('other', 'other'),
       )

MARITAL = (
    ('single', 'single'),
    ('married', 'married'),
    ('other', 'other'),
       )

class CrimeRecordQuerySet(models.QuerySet):
    def search(self, query):
        lookup = (
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(middle_name__icontains=query) |
            Q(date_of_birth__icontains=query) |
            Q(state_of_origin__icontains=query) |
            Q(nationality__icontains=query) |
            Q(extra_note__icontains=query) |
            Q(created__icontains=query) |
            Q(BVN__icontains=query)
        )
        return self.filter(lookup)


class CrimeRecordManager(models.Manager):
    def get_queryset(self):
        return CrimeRecordQuerySet(self.model, using=self._db)

    def search(self, query=None):
        if query is None:
            return self.get_queryset().none()
        return self.get_queryset().search(query)


class CrimeRecord(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    passport = models.ImageField(upload_to='offenders_images/', blank=True, null=True)
    date_of_birth = models.DateField()
    state_of_origin = models.CharField(max_length=40)
    nationality = models.CharField(max_length=40, default='Nigeria')
    BVN = models.CharField(max_length=10, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    sex = models.CharField(max_length=10, choices=SEX, blank=True, null=True)
    marital = models.CharField('Marital Status', max_length=10, choices=MARITAL, blank=True, null=True)
    eye_colour = models.CharField(blank=True, null=True, max_length=20)
    hair_colour = models.CharField(blank=True, null=True, max_length=20)
    height = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)
    extra_note = models.TextField(max_length=300, null=True, blank=True)
    modified = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    # sentence = models.ForeignKey(SentencingInfo, on_delete=models.CASCADE, null=True, blank=True, related_name='criminal')

    objects = CrimeRecordManager()

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return f'{self.first_name} {self.last_name} ({self.created})'


class SentencingInfo(models.Model):
    date = models.DateField()
    offence = models.CharField(max_length=70)
    entity = models.CharField(max_length=75)
    charge = models.CharField(max_length=70)
    term = models.CharField(max_length=20, null=True, blank=True)
    criminal = models.ForeignKey(CrimeRecord, on_delete=models.CASCADE, related_name='sentences', null=True, blank=True)

    class Meta:
        ordering = ('-date',)

