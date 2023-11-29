from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=30)
    statement = models.TextField()
    input_format = models.TextField()
    output_format = models.TextField()
    example = models.TextField()
    # testcases
    timelimit = models.IntegerField(default=1000)
