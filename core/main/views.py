from django.shortcuts import render, redirect
# Create your views here.

mylist = ['homework', 'gym']


def index(request):
    if request.method == 'POST':
        delete_todo = request.POST.get('todo')
        mylist.remove(delete_todo)
        return redirect('home')
    return render(request, 'main/index.html', context={
        'todo': mylist,
    })

def new(request):
    if request.method == 'POST':
        new_todo = request.POST.get('todo')
        mylist.append(new_todo)
        return redirect('home')
    return render(request, 'main/new.html', context={
        
    }) 