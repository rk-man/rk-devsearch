from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from users.models import Profile
from django.contrib import messages
# from django.contrib.auth.forms import UserCreationForm
from users.forms import CustomUserCreationForm
from users.forms import ProfileForm, SkillForm
from django.contrib.auth.decorators import login_required


def profiles(req):
    profiles = Profile.objects.all()
    context = {"profiles": profiles}
    return render(req, "users/profiles.html", context)


def userProfile(req, pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description__exact="")
    otherSkills = profile.skill_set.filter(description="")

    context = {"profile": profile, "topSkills": topSkills,
               "otherSkills": otherSkills}
    return render(req, "users/user_profile.html", context)


def loginUser(req):
    page = 'login'

    if (req.user.is_authenticated):
        return redirect("profiles")

    # 1. get the username and password (default django auth)
    # 2. get the user based on username
    # 3. if no user found with username, throw a message
    # 4. if user, authenticate the user
    # authenticate() -> returns the user found with the email and password
    # 5. if authenticated, then throw a message
    # login() creates a session_id if the authentication is successfull
    # 6. Else throw a message

    if (req.method == "POST"):
        username = req.POST['username']
        password = req.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(req, "Username doesn't exist")
            print("username doesn't exist")
            return redirect('/login')

        user = authenticate(req, username=username, password=password)

        if (user is not None):
            login(req, user)
            return redirect('user-account')
        else:
            print("username or password is incorrect")
            messages.error(req, "username or password is incorrect")

    context = {"page": page}
    return render(req, 'users/login_register.html', context)


def logoutUser(req):
    # removes the session_id
    logout(req)
    messages.info(req, "User was successfully logged out")
    return redirect('login')


def registerUser(req):
    page = 'register'
    form = CustomUserCreationForm()

    if (req.method == "POST"):
        form = CustomUserCreationForm(req.POST)
        print(form)
        if (form.is_valid()):
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(req, "User created successfully")
            login(req, user)
            return redirect('user-account')
        else:
            messages.error(req, "An error has occured during registration")
            # return redirect("register")
    context = {"page": page, "form": form}
    return render(req, "users/login_register.html", context)


@login_required(login_url="login")
def userAccount(req):
    # since profile and user has 1-1 relationship, to access profile from user, we use req.user.profile
    # I can access req.user only when we use login_required() decorator
    profile = req.user.profile
    skills = profile.skill_set.all
    projects = profile.project_set.all()

    context = {"profile": profile, "skills": skills, "projects": projects}
    return render(req, "users/account.html", context)


@login_required(login_url="login")
def editAccount(req):
    profile = req.user.profile
    form = ProfileForm(instance=profile)
    if (req.method == "POST"):
        form = ProfileForm(req.POST, req.FILES, instance=profile)
        if (form.is_valid):
            form.save()

            return redirect("user-account")

    context = {"form": form}
    return render(req, 'users/profile_form.html', context)


@login_required(login_url="login")
def createSkill(req):
    profile = req.user.profile
    form = SkillForm()

    if (req.method == "POST"):
        form = SkillForm(req.POST)
        if (form.is_valid()):
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()
            messages.success(req, "Skill has been created successfully")
            return redirect("user-account")

    context = {"form": form}
    return render(req, "users/skill_form.html", context)


@login_required(login_url="login")
def updateSkill(req, pk):
    profile = req.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance=skill)
    if (req.method == "POST"):
        form = SkillForm(req.POST, instance=skill)
        if (form.is_valid()):
            form.save()
            messages.success(req, "Skill has been updated successfully")
            return redirect("user-account")

    context = {"form": form}
    return render(req, "users/skill_form.html", context)


@login_required(login_url="login")
def deleteSkill(req, pk):
    skill = req.user.profile.skill_set.get(id=pk)
    # skill.delete()
    if (req.method == "POST"):
        skill.delete()
        return redirect("user-account")
    context = {"object": skill}
    return render(req, "delete_temp.html", context)
