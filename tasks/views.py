from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm # Crear Formulario
from django.contrib.auth.models import User  # registrar usuarios
from django.contrib.auth import login, logout,  authenticate#Para crear cookies
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required # Para evitar que un usuario no logeado entre a cualquier ruta que nosotros no queramos
# Create your views here.


def home(request):

    return render(request, 'home.html')

@login_required #ir al archivo settings.py de la carpeta main e crear una variable llamada LOGIN_URL = 'vista a la que quieras que vaya' (se crear al final debajo de static_url)
def task_detail(request, task_id):
    if request.method == 'GET':

        task = get_object_or_404(Task, pk=task_id, user=request.user) #pk = PrimaryKey
        form = TaskForm(instance=task)
        return render(request, 'task_detail.html', { 'task': task, 'form' : form})
    
    else:
        try:



            task = get_object_or_404(Task, pk=task_id, user=request.user) #pk = PrimaryKey
            form = TaskForm(request.POST ,instance=task)
            form.save()
            return redirect('task')
        
        except ValueError:

            return render(request, 'task_detail.html', { 'task': task, 'form' : form, 'error': "ERROR TRY IT AGAIN"})
    
@login_required
def create_task(request):

    if request.method == 'GET':

        return render(request, 'create_task.html', {
            'form' : TaskForm
        })
    
    else:
        try:
            form = TaskForm(request.POST)
            new_task = form.save(commit=False) #Commit=false significa no guardar en la base de datos todavia debido a que se esta usando, segun chatgpt xD
            new_task.user = request.user
            new_task.save()
            return redirect('task')
        
        except ValueError:


             return render(request, 'create_task.html', {
                'form' : TaskForm,
                'error': "Invalid Data"
            })
    
@login_required
def tasks(request):
    try:
        tasks = Task.objects.filter(user=request.user, datecompleted__isnull=True) #datecompleted__isnull=True # Esto de filter() Es para ver solo las tareas del usuario logeado/actual (SE PUEDEN USAR MAS PARAMETROS DENTRO DEL FILTER)

        return render(request, 'task.html', {
            'tasks' : tasks
        })
    except:
        return render(request, 'home.html', {
            'error' : "Debes registrarte si quieres ingresar al modulo de tareas"
        })

@login_required
def task_complete(request, task_id):

    task =get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'POST':
        task.datecompleted = timezone.now()
        task.save()
        return redirect('task')
    
@login_required
def task_delete(request, task_id):
    task =get_object_or_404(Task, pk=task_id, user=request.user)

    if request.method == 'POST':
        task.delete()
        return redirect('task_completed')

@login_required
def task_completed(request):
    tasks = Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by('-datecompleted')

    return render(request, 'task.html', {'tasks': tasks})

def signin(request):

    if request.method == 'GET':

        return render(request, 'signin.html', {
            'authentication': AuthenticationForm
        })
    else:
        print(request.POST)
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
    

        if user is None:

            return render(request, 'signin.html', {
                'error': "Incorrect account name or password.",
                'authentication': AuthenticationForm
            })
        
        else:
            login(request, user)
            return redirect('home')

def signout(request): #No se puede nombrar logout la funcion xq traeria conflictos
    logout(request)
    return redirect('home')

def signup(request):
    if request.method == 'GET':

        return render(request, 'signup.html', {

            'form': UserCreationForm
        })

    else:
        if request.POST['password1'] == request.POST['password2']:
            # Register user
            try:
                # Espera 2 argumentos, usuario y contrase;a del usuario
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user) #Para autenticar usuario (cookie)
                return render(request, 'home.html', {
                    "welcome": 'You have created a new user'
                })

            #except IntegrityError ( debes importar el error arriba)
            except:

                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    "error": 'The username is already taken'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            "error": 'Passwords do not match'
        })

