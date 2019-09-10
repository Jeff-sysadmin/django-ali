from rest_framework import serializers
from recruit_api.apps.job.models import Job
from recruit_api.apps.job.models.job import Skills


class JobskillSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        exclude = ('created', 'modified')

class JobSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()
    category_name = serializers.SerializerMethodField()
    skill_name = serializers.SerializerMethodField()
    def get_client_name(self, job):
        return job.client.name

    def get_category_name(self, job):
        return job.category.title

    def get_skill_name(self, job):
        if job.skills:
            skl=job.skills.split(',')
            return Skills.objects.filter(id__in=skl).values()
        else:
            return []
        return job.category.title

    class Meta:
        model = Job
        exclude = ('created', 'modified')




class JobListSerializer(serializers.ModelSerializer):
    client_name = serializers.SerializerMethodField()

    def get_client_name(self, job):
        return job.client.name

    class Meta:
        model = Job
        fields = ("id", "employment_type", "status", "title", "location", "min_salary", "max_salary", "skills",
                  "short_description", "long_description", "publish_at", "publish_until", "short_description_public",
                  "employment_type_public", "annual_pay_public", "long_description_public", "location_public", "client",
                  "client_name", "category", "intake_call", "candidate_feedback", "companies_hiring", "template_email",
                  "hiring_manager","third_party_bill_rate", "visa_1099_bill_rate","green_card_bill_rate","citizen_bill_rate")
