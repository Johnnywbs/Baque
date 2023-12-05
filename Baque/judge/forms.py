from django import forms
from .models import Problem, Submission, TestCase, TestCaseGenerator

class TestCaseForm(forms.ModelForm):
    class Meta:
        model = TestCase
        fields = ['input_data', 'expected_output']

    def __init__(self, *args, **kwargs):
        super(TestCaseForm, self).__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].widget.attrs.update({'class': 'form-control'})


ProblemFormSet = forms.inlineformset_factory(Problem, TestCase, form=TestCaseForm, extra=5)

class ProblemForm(forms.ModelForm):
    class Meta:
        model = Problem
        fields = "__all__"

class SubmissionForm(forms.ModelForm):
    class Meta:
        model = Submission
        fields = ['code']

class TestCaseGeneratorForm(forms.ModelForm):
    class Meta:
        model = TestCaseGenerator
        fields = ['generator_code', 'number_of_testcases']

