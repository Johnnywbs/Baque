from django.db import models

class Problem(models.Model):
    name = models.CharField(max_length=30)
    statement = models.TextField()
    input_format = models.TextField()
    output_format = models.TextField()
    example = models.TextField()
    timelimit = models.IntegerField(default=1000)

    def __str__(self):
        return f'{self.id}. {self.name}'

class TestCase(models.Model):
    problem = models.ForeignKey("Problem", on_delete=models.CASCADE)
    input_data = models.TextField()
    expected_output = models.TextField()

class Submission(models.Model):
    problem = models.ForeignKey("Problem", on_delete=models.CASCADE)
    code = models.FileField(upload_to="code/")

class Result(models.Model):
    submission = models.ForeignKey("Submission", on_delete=models.CASCADE)
    testcase = models.ForeignKey("TestCase", on_delete=models.CASCADE)
    passed = models.BooleanField()
    actual_output = models.TextField()
