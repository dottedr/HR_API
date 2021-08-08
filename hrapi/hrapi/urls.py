from django.contrib import admin
from django.urls import path, include, re_path

from rest_framework import routers
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls

from hr.views import ProfileSingle, ProfilesList, AverageAge, AverageSalary, AverageSalaryPerExperience, SalaryPredictor

router = routers.SimpleRouter()

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),

    path('v1/profiles/', ProfilesList.as_view()),
    path('v1/profiles/<int:pk>/', ProfileSingle.as_view()),

    path('v1/age/<str:industry>', AverageAge.as_view()),
    path('v1/salary/industry/<str:industry>', AverageSalary.as_view()),
    path('v1/salary/experience/<int:experience>', AverageSalaryPerExperience.as_view()),
    path('v1/salary/prediction/<int:gender>/<int:industry>/<int:experience>/<int:age>', SalaryPredictor.as_view()),


    path('v1/docs/', include_docs_urls(title="HR API")),
    # API schema used for docs generation
    path('v1/schema/', get_schema_view(
        title='HR API',
        description='API for the HR API',
        version="1.0.0"
    ), name='openapi=schema'),
]
