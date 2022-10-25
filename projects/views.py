from projects.models import Project

from django.shortcuts import render, redirect

from projects.forms import ProjectForm
from django.contrib.auth.decorators import login_required


def projects(req):
    allProjects = Project.objects.all()
    # print(allProjects)
    return render(req, "projects/projects.html", {"allProjects": allProjects})


def getProject(req, pk):
    projectObj = Project.objects.get(id=pk)
    tags = projectObj.tags.all()

    # print(projectObj)

    return render(req, "projects/singleProject.html", {"msg": "Hello there", "project": projectObj, "tags": tags})


@login_required(login_url="login")
def createProject(req):
    profile = req.user.profile
    form = ProjectForm()

    if (req.method == 'POST'):
        # this creates the object and returns queryDict
        # req.POST contains the data
        form = ProjectForm(req.POST, req.FILES)
        # print(form)

        if (form.is_valid()):
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('user-account')  # redirect to the url name

    context = {'form': form}
    return render(req, "projects/project_form.html", context)


@login_required(login_url="login")
def updateProject(req, pk):
    profile = req.user.profile

    # to make sure that the person created the project can update the project
    project = profile.project_set.get(id=pk)

    # pass the exisiting object to the ProjectForm which
    # fills the returned object with instance
    form = ProjectForm(instance=project)
    # print(form)
    context = {"form": form}

    if (req.method == 'POST'):
        # this updates the object and returns queryDict
        # req.POST contains the data
        form = ProjectForm(req.POST, req.FILES, instance=project)
        # print(form)

        if (form.is_valid()):
            form.save()  # saves to the database
            return redirect('user-account')  # redirect to the url name

    context = {'form': form}
    return render(req, "projects/project_form.html", context)


@login_required(login_url="login")
def deleteProject(req, pk):
    profile = req.user.profile
    project = profile.project_set.get(id=pk)
    context = {"object": project}

    if (req.method == 'POST'):
        project.delete()
        return redirect("user-account")

    return render(req, "delete_temp.html", context)
