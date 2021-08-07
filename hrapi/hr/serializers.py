from rest_framework import serializers

from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id', 'first_name','last_name', 'email', 'gender', 'date_of_birth', 'industry', 'salary', 'years_of_experience')