from django.shortcuts import render

from .forms import ToDoForm

# Create your views here.
def show_demo(request):
    form = ToDoForm()
    return render(request, 'myapp/my_template.html', {'form': form})

