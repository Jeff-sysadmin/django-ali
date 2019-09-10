from django.db import models
from django.core.validators import (MinLengthValidator, MinValueValidator)
from model_utils.models import TimeStampedModel
from recruit_api.apps.category.models import Category
from recruit_api.apps.client.models import Client
from recruit_api.apps.job.constants import (EMPLOYMENT_TYPE_CHOICES, DEFAULT_EMPLOYMENT_TYPE,
                                            STATUS_CHOICES, DEFAULT_STATUS)


class Skills(TimeStampedModel):
    title = models.CharField(max_length=255)


class Job(TimeStampedModel):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    employment_type = models.IntegerField(choices=EMPLOYMENT_TYPE_CHOICES, default=DEFAULT_EMPLOYMENT_TYPE)
    status = models.IntegerField(choices=STATUS_CHOICES, default=DEFAULT_STATUS)
    title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    skills = models.CharField(max_length=500, null=True, blank=True)
    min_salary = models.IntegerField(validators=[MinValueValidator(0)])
    max_salary = models.IntegerField(validators=[MinValueValidator(0)])
    third_party_bill_rate = models.CharField(max_length=255, null=True, blank=True, default="1.18")
    visa_1099_bill_rate = models.CharField(max_length=255, null=True, blank=True, default="1.15")
    citizen_bill_rate = models.CharField(max_length=255, null=True, blank=True, default="1.18")
    green_card_bill_rate = models.CharField(max_length=255, null=True, blank=True, default="1.18")
    short_description = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    long_description = models.TextField(validators=[MinLengthValidator(10)])
    intake_call = models.TextField(blank=True, null=True)
    candidate_feedback = models.TextField(blank=True, null=True)
    companies_hiring = models.TextField(blank=True, null=True)
    template_email = models.TextField(blank=True, null=True)
    hiring_manager = models.TextField(blank=True, null=True)
    publish_at = models.DateField(null=True, blank=True)
    publish_until = models.DateField(null=True, blank=True)
    short_description_public = models.BooleanField(default=True)
    employment_type_public = models.BooleanField(default=True)
    annual_pay_public = models.BooleanField(default=True)
    long_description_public = models.BooleanField(default=True)
    location_public = models.BooleanField(default=True)

    class Meta:
        app_label = "job"
        verbose_name_plural = "Jobs"
        ordering = ['title']

    def __str__(self):
        return self.title

    @property
    def salary(self):
        return f'${self.min_salary}k-${self.max_salary}k'

    @property
    def publish_at_formatted(self):
        return 'N/A' if not self.publish_at else self.publish_at.strftime('%d/%m/%Y')
