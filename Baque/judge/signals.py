import subprocess

def run_code(code, input_data, timelimit):
    try:
        stdout = subprocess.check_output(['python3', '-c', code], input=input_data, stderr=subprocess.STDOUT, text=True, timeout=timelimit/1000)
        return stdout, ''
    except subprocess.CalledProcessError:
        return '', 'RTE'
    except subprocess.TimeoutExpired:
        return '', 'TLE'

from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Submission, TestCase, Result

@receiver(post_save, sender=Submission)
def run_test_cases(sender, instance, **kwargs):
    submission = instance
    problem = submission.problem
    test_cases = TestCase.objects.filter(problem=problem)

    for case in test_cases:
        input_data = case.input_data
        expected_output = case.expected_output

        code = ""
        with open(submission.code.path, 'r') as file: code = file.read()

        actual_output, err = run_code(code, input_data, submission.problem.timelimit)
        if err == 'TLE':
            verdict = 'time_limit_exceeded'
        elif err == 'RTE':
            verdict = 'runtime_error'
            actual_output = err
        else:
            actual_output = ' '.join(actual_output.split())
            expected_output = ' '.join(expected_output.split())
            passed = actual_output == expected_output
            verdict = 'accepted' if passed else 'wrong_answer'

        Result.objects.update_or_create(
            submission=submission,
            testcase=case,
            defaults={
                'passed' : verdict == 'accepted',
                'actual_output': actual_output,
                'verdict': verdict
            }
        )

from .models import TestCaseGenerator, Problem

@receiver(post_save, sender=TestCaseGenerator)
def generate_testcases(sender, instance, **kwargs):
    for i in range(instance.number_of_testcases):
        with open(instance.generator_code.path, 'r') as file: code = file.read()
        generated_input, err = run_code(code, '', 1000)
        if err: continue

        expected_output, err = run_code(instance.problem.model_solution, generated_input, instance.problem.timelimit)
        if err: continue

        TestCase.objects.create(
            problem=instance.problem,
            input_data=generated_input,
            expected_output=expected_output
        )
