from rest_framework import generics
from rest_framework import mixins
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.filters import OrderingFilter

from django_filters.rest_framework import DjangoFilterBackend

from django.db import connection

from .models import Profile
from .serializers import ProfileSerializer

import pandas as pd


# Using class based views to use mixins and generics
class ProfilesList(mixins.ListModelMixin,
                   generics.GenericAPIView):
    """
    Lists all users.

    Pagination:
    URI parameter: page
    Default page size is set to 100 in setting.py as 'PAGE_SIZE'

    Filtering:
    URI parameters: first_name,last_name, email, gender, date_of_birth, industry, salary, years_of_experience

    Sorting:
    URI parameter: industry, salary, years_of_experience

    More docs: https://www.django-rest-framework.org/api-guide/filtering/
    """
    # applying new properties by using attributes
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['first_name', 'last_name', 'email', 'gender', 'date_of_birth', 'industry', 'salary',
                        'years_of_experience']
    ordering_fields = ['industry', 'salary', 'years_of_experience']

    def get(self, request):
        return self.list(self, request)


class ProfileSingle(mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    generics.GenericAPIView):
    """ Class responsible for handling requests for one profile at the time """
    serializer_class = ProfileSerializer
    queryset = Profile.objects.all()

    # I prefer to avoid *args and **kwargs to avoid less optimal design decisions later
    # In case of simple get, put and delete request I don't see a need for *args and **kwargs
    # However, if there were many arguments I would use *args and **kwargs
    def get(self, request, pk):
        """ Gets a single profile

        Parameters:
        pk (int): profile ID, primary key in the database

        """
        return self.retrieve(request, pk)

    def put(self, request, pk):
        """ Updates a single profile """
        return self.update(request, pk)

    def delete(self, request, pk):
        """ Deletes a single profile """
        return self.destroy(request, pk)


class AverageAge(APIView):
    """
    Calculates average age in given industry
    URI path: v1/age/<str:industry>
    """

    def get(self, request, industry: str):
        """
        Gets a single age average

        Parameters:
        industry (str): industry of interest, one of the listed in the dataframe,
        e.g. Metal Fabrications
        """
        query = str(Profile.objects.all().query)
        df = pd.read_sql(query, connection)
        # select rows with this industry
        industry_df = df[df['industry'] == industry]
        dates = industry_df['date_of_birth'].values
        ages = []
        sum = 0

        for date in dates:
            today = date.today()
            age = today.year - date.year - ((today.month, today.day) < (date.month, date.day))
            ages.append(age)
            sum = sum + age
        avg_age = sum / dates.shape[0]

        data = {
            "industry": industry,
            "average_age": avg_age
        }

        return Response(data)


class AverageSalary(APIView):
    """
    Calculates average salary in given industry
    URI path: v1/salary/industry/<str:industry>
    """

    def get(self, request, industry: str):
        query = str(Profile.objects.all().query)
        df = pd.read_sql(query, connection)

        industry_df = df[df['industry'] == industry]
        salaries = industry_df['salary']
        avg_salary = salaries.sum() / industry_df.shape[0]

        data = {
            "industry": industry,
            "average_salary": avg_salary
        }

        return Response(data)


class AverageSalaryPerExperience(APIView):
    """
    Calculates average salary per years of experience
    URI path: v1/salary/industry/<int:experience>
    """

    def get(self, request, experience: int):
        query = str(Profile.objects.all().query)
        df = pd.read_sql(query, connection)

        experience_df = df[df['years_of_experience'] == experience]
        salary_per_experience = experience_df['salary']
        avg_salary_per_experience = salary_per_experience.sum() / experience_df.shape[0]

        data = {
            "years_of_experience": experience,
            "average_salary_per_experience": avg_salary_per_experience
        }

        return Response(data)
