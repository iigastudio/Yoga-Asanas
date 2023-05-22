from django.shortcuts import render

from django.shortcuts import redirect

from .forms import PoseForm

from .models import Pose

from django.contrib.auth.models import User

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


def loginPage(request):
    page = 'login'

    if request.user.is_authenticated:
        return redirect('/')

    # Submitted login form
    if request.method == 'POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            print('User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect('/')
        else:
            print('Invalid username or passwors')

    context = {'page': page}
    return render(request, 'login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].validators = []
        self.fields['password2'].validators = []


def registerUser(request):
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('/')
        else:
            print("Error in registration")

    return render(request, 'login_register.html', {'form': form})


def poses(request):
    poses = Pose.objects.all()

    context = {
        "page_title": "Pose Poses",
        "poses": poses,
    }
    return render(request, "homepage.html", context)


def pose(request, pk):
    pose = Pose.objects.get(id=pk)

    context = {
        "page_title": "Pose Pose",
        "pose": pose,
    }

    return render(request, "pose.html", context)


@login_required(login_url="login")
def addPose(request):
    form = PoseForm()

    '''
        form = PoseForm(request.POST, request.FILES)
        if form.is_valid():

            form.save()
            return HttpResponseRedirect(reverse('poses'))
        else:
            context = {'form': form}
            return render(request, 'pose_form.html', context)
    else:
        form = PoseForm()
        return render(request, 'pose_form.html', {'form':form})
    '''
    if request.method == 'POST':
        Pose.objects.create(
            posted_by=request.user,
            name=request.POST.get('name'),
            level=request.POST.get('level'),
            image=request.FILES['image'],
            description=request.POST.get('description')
        )

        return redirect('/')

    context = {'form': form}
    return render(request, 'pose_form.html', context)


@login_required(login_url="login")
def updatePose(request, pk):
    pose = Pose.objects.get(id=pk)

    form = PoseForm(instance=pose)

    if request.user != pose.posted_by:
        return render(request, "not_authorized.html")

    if request.method == 'POST':
        pose.name = request.POST.get('name')
        pose.level = request.POST.get('level')
        pose.image = request.FILES['image']
        pose.description = request.POST.get('description')

        pose.save()
        return redirect('/')


    context = {'form': form, 'pose': pose}
    return render(request, 'pose_form.html', context)





@login_required(login_url="login")
def deletePose(request, pk):

    pose = Pose.objects.get(id=pk)



    if request.user != pose.posted_by:
        return render(request, "not_authorized.html")

    if request.method == 'POST':

        pose.delete()

        return redirect('/')

    return render(request, 'delete.html', {'obj': pose})
