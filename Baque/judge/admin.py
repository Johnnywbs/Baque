from django.contrib import admin
from .models import Problem, TestCase, Submission, Result

class TestCaseInline(admin.TabularInline):
    model = TestCase

class ResultInline(admin.TabularInline):
    model = Result

@admin.register(Problem)
class ProblemAdmin(admin.ModelAdmin):
    inlines = [TestCaseInline]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    inlines = [ResultInline]

@admin.register(TestCase)
class TestCaseAdmin(admin.ModelAdmin):
    list_display = ('problem', 'input_data', 'expected_output')

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ('submission', 'testcase', 'passed', 'actual_output')

