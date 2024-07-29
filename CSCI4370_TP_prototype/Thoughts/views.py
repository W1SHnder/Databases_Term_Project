from django.shortcuts import render, redirect
from Thoughts.models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages



#Prefetch related means each Thought has a list of tags accessable with ".tags"
#Expects queryset to include only thoughts created by request.user or marked public
def filter_thoughts_by_keyword(keyword, qset):
    filtered_rows = qset.objects.filter(
        Q(title__icontains=keyword) | Q(content__icontains=keyword)
        ).prefetch_related('tags')
    return filtered_rows

#Accepts a tag ID or object and returns all thoughts with that tag
def filter_by_tag(tag, current_user):
    if isinstance(tag, int):
        tag = Tag.objects.get(id=tag)
    filtered_rows = tag.thoughts.all().filter(
        Q(public=True) | Q(user=current_user)
    ).prefetch_related('tags')
    return filtered_rows


def get_popular_tags():
    tags = Tag.objects.annotate(
        num_thoughts=models.Count('thoughts')
        ).order_by('-num_thoughts')
    return tags






def landing(request):
    return render(request, 'landing.html', {})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('form3Example3c')
        password = request.POST.get('form3Example4c')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else: 
            return render(request, 'login.html', {'error': 'Invalid credentials'})
        
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html', {})

def main(request):
    return render(request, 'main.html', {})