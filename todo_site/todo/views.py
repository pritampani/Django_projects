from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import TodoForm
from .models import TodoItem

def index(request):
    item_list = TodoItem.objects.order_by("-date")
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = TodoForm()

    page = {
        "form": form,
        "list": item_list,
        "title": "TODO LIST",
    }
    return render(request, 'todo/index.html', page)

def remove(request, item_id):
    item = get_object_or_404(TodoItem, pk=item_id)
    item.delete()
    messages.info(request, "Item removed !!!")
    return redirect('index')
