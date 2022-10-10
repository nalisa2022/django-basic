from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class register_patientinfo_db(models.Model):
    name=models.CharField(max_length=255, null=False)
    ename=models.CharField(max_length=255, null=False)
    # birth=models.CharField(max_length=255, null=False)