from django.db import models
from django.core.validators import (MinLengthValidator, MinValueValidator)
from model_utils.models import TimeStampedModel
from recruit_api.apps.client.constants import (EMPLOYEE_COUNT_CHOICES, DEFAULT_EMPLOYEE_COUNT)
from recruit_api.apps.core.user.models import User
from recruit_api.apps.candidate.constants import (CANDIDATE_STATUS_CHOICES, DEFAULT_CANDIDATE_STATUS,
                                                  VISA_STATUS_CHOICES, DEFAULT_VISA_STATUS)


class RecruitMinLengthValidator(MinLengthValidator):
    def compare(self, a, b):
        return int(a) < int(b)

    def clean(self, x):
        return len(str(x))


class ContactPhone(TimeStampedModel):
    phone = models.CharField(max_length=255)

    class Meta:
        app_label = "candidate"
        verbose_name_plural = 'Phone(s)'

    def __str__(self):
        return self.phone

class ContactEmail(TimeStampedModel):
    email = models.EmailField()

    class Meta:
        app_label = "candidate"
        verbose_name_plural = 'Email(s)'

    def __str__(self):
        return self.email


class Contact(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    phone = models.ManyToManyField(ContactPhone, blank=True)
    email = models.ManyToManyField(ContactEmail, blank=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    notes = models.TextField(max_length=255, blank=True, null=True)
    recruiter = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    status = models.IntegerField(choices=CANDIDATE_STATUS_CHOICES, default=DEFAULT_CANDIDATE_STATUS)
    created=models.DateField(blank=True, null=True)
    modified=models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return '{} - {}'.format(self.name, self.email)


class Client(TimeStampedModel):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255, blank=True, null=True)
    founded_year = models.IntegerField(validators=[MinValueValidator(0), RecruitMinLengthValidator(4)], blank=True, null=True)
    website = models.URLField(max_length=500, blank=True, null=True)
    employee_count = models.IntegerField(choices=EMPLOYEE_COUNT_CHOICES, default=DEFAULT_EMPLOYEE_COUNT)
    logo_url = models.URLField(max_length=500, blank=True, null=True)
    company_info = models.TextField(blank=True, null=True)
    competitors = models.TextField(blank=True, null=True)
    selling_points = models.TextField(blank=True, null=True)
    products = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    contact = models.ManyToManyField(Contact, blank=True)
    fee = models.IntegerField(null=True, blank=True)

    class Meta:
        app_label = "client"
        ordering = ['name']
        verbose_name_plural = "Clients"


    def __str__(self):
        return self.name
