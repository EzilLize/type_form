from django.shortcuts import render, HttpResponse
from danis import forms

posts = []


def index(request):
    return render(request, 'index.html',
                  {'posts': posts})


def create(request):
    if request.method == 'POST':
        header = request.POST.get('header')
        content = request.POST.get('content')
        is_publish = request.POST.get('is_publish')
        date = request.POST.get('date')
        post = {}
        post['header'] = header
        post['content'] = content
        post['date'] = date
        if not is_publish:
            return HttpResponse('<h2>Post cannot be published</h2>')
        posts.append(post)
        return HttpResponse(f"<h2>Post added under number{len(posts)}</h2>")
    else:
        post = forms.PostForm()
    return render(request, 'create.html', {'form': post})