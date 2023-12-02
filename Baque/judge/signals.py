import subprocess

def run_code(code, input_data):
    process = subprocess.Popen(['python', '-c', code], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate(input_data)
    return stdout, stderr

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Submission, TestCase, Result

@receiver(post_save, sender=Submission)
def run_test_cases(sender, instance, **kwargs):
    submission = instance
    problem = submission.problem
    test_cases = TestCase.objects.filter(problem=problem)

    for test_case in test_cases:
        input_data = test_case.input_data
        expected_output = test_case.expected_output

        code = ""
        with open(submission.code.path, 'r') as file:
            code = file.read()

        actual_output, error_output = run_code(code, input_data)
        actual_output = ' '.join(actual_output.split())
        expected_output = ' '.join(expected_output.split())

        passed = actual_output == expected_output

        Result.objects.create(submission=submission, testcase=test_case, passed=passed, actual_output=actual_output)

