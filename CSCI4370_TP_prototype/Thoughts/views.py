from django.shortcuts import render, redirect
from Thoughts.models import *
from django.db.models import Q
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.generic import TemplateView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_http_methods



#Prefetch related means each Thought has a list of tags accessable with ".tags"
#Expects queryset to include only thoughts created by request.user or marked public
def filter_thoughts_by_keyword(keyword, qset):
    filtered_rows = qset.objects.filter(
        Q(title__icontains=keyword) | Q(content__icontains=keyword)
        )
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

@require_http_methods(["GET", "POST"])
def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
        elif User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, 'User created successfully')
            return redirect('login')
    return render(request, 'signup.html')

class MainView(LoginRequiredMixin, ListView):
    template_name = 'main.html'
    login_url = "/login"

    def get_queryset(self):
        return Thought.objects.filter(Q(user=self.request.user) | Q(public=True)).prefetch_related('tags')

    


#def main(request):
  #  return render(request, 'main.html', {})