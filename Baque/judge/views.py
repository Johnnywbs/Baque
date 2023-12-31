from django.shortcuts import render, redirect, get_object_or_404
from .models import Problem, Submission, Result
from .forms import ProblemForm, ProblemFormSet, SubmissionForm, TestCaseGeneratorForm
from django.db.models import Count, Q

def index(request):
    return render(request, "judge/index.html")

def problem_list(request):
    problems = Problem.objects.all()
    return render(request, "judge/problem_list.html", {'problems' : problems})

def submission_list(request):
    submissions = Submission.objects.all()
    submission_data = []

    for submission in submissions:
        total_results = Result.objects.filter(submission=submission).count()
        passed_results = Result.objects.filter(submission=submission,passed=True).count()

        submission_data.append({
            'id' : submission.id,
            'problem_name' : submission.problem.name,
            'passed_results' : passed_results,
            'total_results' : total_results,
        })

    return render(request, "judge/submission_list.html", {'submissions' : submission_data})

def edit(request, id=None):
    if id is not None:
        problem = get_object_or_404(Problem, id=id)
    else:
        problem = None

    if request.method == "POST":
        form = ProblemForm(request.POST, instance=problem)
        formset = ProblemFormSet(request.POST, instance=problem)

        if form.is_valid() and formset.is_valid():
            problem = form.save()
            formset.instance = problem
            formset.save()
            return redirect('problem', problem.id)
    else:
        form = ProblemForm(instance=problem)
        formset = ProblemFormSet(instance=problem)

    return render(request, "judge/edit.html", {'form': form, 'formset': formset, 'problem': problem})

def problem(request, id):
    p = get_object_or_404(Problem, pk=id)

    if request.method == "POST":
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.problem = p
            submission.save()
            return redirect('submission', submission.id)
    else:
        form = SubmissionForm()

    return render(request, "judge/problem.html", {'problem': p, 'form': form})

def add_generator(request, id):
    problem = get_object_or_404(Problem, pk=id)
    if request.method == "POST":
        form = TestCaseGeneratorForm(request.POST, request.FILES)
        if form.is_valid():
            generator = form.save(commit=False)
            generator.problem = problem
            generator.save()
            return redirect('problem', id=id)
    else:
        form = TestCaseGeneratorForm()
    return render(request, 'judge/add_generator.html', {'form':form, 'problem':problem})

def submission(request, id):
    submission = get_object_or_404(Submission, pk=id)
    results = Result.objects.filter(submission=submission)

    context = {
            'submission' : submission,
            'results' : results,
    }

    return render(request, "judge/submission.html", context)
