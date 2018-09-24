from django.shortcuts import render, redirect
from apps.login_registration.models import User
from apps.handy_helper.models import Job
from django.contrib import messages

def index(request):
    print('\n\n** Showing Dashboard INdex')
    all_jobs = Job.objects.exclude(workers__id=request.session["user_id"])
    jobs_helping = Job.objects.filter(workers__id=request.session['user_id'])
    u = User.objects.get(id=request.session['user_id'])

    context = {
        "jobs" : all_jobs,
        "my_jobs" : jobs_helping,
        "user" : u
    }
    return render(request, "handy_helper/index.html", context)

def view(request, id):
    print(f'\n\n** Viewing Job #{id}')
    j = Job.objects.get(id=id)

    print(j)
    context = {
        'job' : j
    }
    return render(request, 'handy_helper/view.html', context)

def help(request, id):
    print(f"Helping wiht Job #{id}")
    j = Job.objects.get(id=id)
    u = User.objects.get(id=request.session['user_id'])

    j.workers.add(u)

    return redirect('/')



def add(request):
    print('\n\n** Showing Add Form')
    context = {}
    return render(request, 'handy_helper/add.html', context)

def create_job(request):
    print('\n\n** Processing creating job')
    print(request.POST)

    errors = Job.objects.validateNewJob(request.POST)

    if len(errors):
        print("ERRORS!")
        for k, message in errors.items():
            messages.error(request, message)
        return redirect("/dashboard/add")
    print("Creating new Job")
    u = User.objects.get(id=request.session['user_id'])
    j = Job.objects.create(title = request.POST['title'], description = request.POST["description"], location = request.POST["location"], creator = u)
    print(j)
    return redirect('/dashboard')

def edit(request, id):
    print(f'\n\n** Showing Edit Form for Job #{id}')

    j = Job.objects.get(id=id)
    context = {
        "job" : j,
    }
    return render(request, 'handy_helper/edit.html', context)

def update(request, id):
    print(f"Updating Job #{id}")
    errors = Job.objects.validateNewJob(request.POST)
    j = Job.objects.get(id=id)
    if len(errors):
        print("ERRORS!")
        for k, message in errors.items():
            messages.error(request, message)
        return redirect(f"/dashboard/edit/{id}")

    print('No errors! Updating!')
    j.title = request.POST['title']
    j.description = request.POST['description']
    j.location = request.POST['location']
    j.save()

    return redirect('/')

def delete_job(request, id):
    print(f"\n\n** Deleting Job #{id}")
    u = User.objects.get(id=request.session["user_id"])
    j = Job.objects.get(id=id)

    if(j.creator == u):
        j.delete()
    else:
        messages.error(request, f"Cannot delete job you didn't create")
    return redirect('/')

def complete(request, id):
    print(f"\n\n** Completing Job #{id}")
    j = Job.objects.get(id=id)

    j.delete()
    return redirect('/')
