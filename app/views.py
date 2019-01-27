from django.shortcuts import render,redirect,get_object_or_404
from .models import posts,contact
from django.views import generic
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate

'''class home(generic.ListView):
    model = posts
    #context_object_name = 'all_posts'
    queryset = posts.objects.all()
    template_name = 'index.html'
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(home,self).get_context_data(**kwargs)
        context['all_posts'] = posts.objects.all()
        context['some_posts'] = posts.objects.all()[:1]
        return context'''

def login(request):
    if request.method == 'POST':
        uname = request.POST['uname']
        passwd = request.POST['pass']
        user = authenticate(username = uname,password = passwd )
        if user is not None:
            return redirect('/admin')
        else:
            return render(request,'login.html',{'message':'Invalid Username or Password'})
    return render(request,'login.html',{'message':''})

def home(request):
    post = posts.objects.all().order_by('-date')
    paginator = Paginator(post,3)
    pageno = request.GET.get('pageno')
    post = paginator.get_page(pageno)
    return render(request,'index.html',{'all_posts':post,})

def about(request):
    return render(request,'about.html')

def retposts(request):
    post = posts.objects.all()
    paginator = Paginator(post,3)
    pageno = request.GET.get('pageno')
    post = paginator.get_page(pageno)
    return render(request,'allposts.html',{'all_posts':post,})

def retcontact(request):
    return render(request,'contact.html')

def idposts(request,post_id):
    post = get_object_or_404(posts,pk=post_id)
    path = "/static/img/posts_img/"+post.img_file
    return render(request,'post.html',{'post':post,'imgpath':path})

'''class idposts(generic.ListView):
    model = posts
    template_name = 'post1.html'
    context_object_name = 'post'
    queryset = posts.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some_posts'] = posts.objects.filter(pk=self.kwargs['p'])
        return context'''
