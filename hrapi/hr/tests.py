from django.test import TestCase

# Create your tests here.

# Case 1 : yy = avg_age('Metal Fabrications') 60.76923076923077

import pytest

from django.contrib.auth.models import User

@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test','test@test.com','password')
    count = User.objects.all().count()
    print(count)
    assert User.objects.count() == 1

