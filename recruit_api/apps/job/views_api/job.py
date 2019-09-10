from rest_framework import status
from rest_framework.decorators import api_view
from recruit_api.apps.utils.models import ResponseData
from recruit_api.apps.utils.api.response import RecruitResponse
from recruit_api.apps.job.operations import JobOperations
from rest_framework import generics
from rest_framework import viewsets
from recruit_api.apps.job.models import *
from recruit_api.apps.job.serializers import JobSerializer
from django.db.models import Q

class JobView(viewsets.ModelViewSet):
    serializer_class = JobSerializer
    queryset = Job.objects.all()
    def get_queryset(self):
        page=self.request.query_params.get('page')
        client = self.request.query_params.get('client')
        if client:
            queryset = Job.objects.filter(client=client)
            #queryset = Job.objects.all()
        else:
            location = self.request.query_params.get('location')
            category = self.request.query_params.get('category')
            skill = self.request.query_params.get('skill')
            term = self.request.query_params.get('terms')
            salary = self.request.query_params.get('salary')
            emptype= self.request.query_params.get('emptype')
            candidates=Job.objects.filter(id__gte=0)
            if term:
                candidates = candidates.filter(
                  Q(title__icontains=term)
                | Q(short_description__icontains=term)
                | Q(long_description__icontains=term))


            if location:
                candidates=candidates.filter(location__icontains=location)

            if category:
                category=category.split(",")
                candidates=candidates.filter(category__id__in=category)
            if emptype:
                allemp=emptype.split(",")
                candidates=candidates.filter(employment_type__in=allemp)

            if salary:
                allemp=salary.split(",")
                minsl=allemp[0]
                maxsl=allemp[1]
                candidates=candidates.filter(min_salary__range=(minsl, maxsl)).filter(max_salary__range=(minsl, maxsl))

            if skill:
                #skill=skill.split(",")
                #candidates=candidates.filter(skills__in=skill)
                candidates=candidates.filter(skills__icontains=skill)
            if page:
                page=int(page)
                endp=page*20
                startp=endp-20
                candidates=candidates[startp:endp]
                
            queryset = candidates.all()
        return queryset
