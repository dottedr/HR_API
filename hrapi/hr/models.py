from django.db import models


class Profile(models.Model):
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    email = models.EmailField(null=True)
    gender = models.CharField(max_length=254, null=True)
    # In case of using Postgres Database and having the date in dd/mm/yyyy format
    # change date format by `SET DateStyle TO European`
    # TODO: Change date format in the code
    date_of_birth = models.DateField(null=True)
    industry = models.CharField(max_length=254, null=True)
    salary = models.FloatField(null=True)
    years_of_experience = models.IntegerField(null=True)

    def __str__(self):
        return "%s %s" % (self.first_name, self.last_name)
