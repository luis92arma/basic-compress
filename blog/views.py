from django.http import HttpResponse, Http404
from django.template import loader, RequestContext
from django.shortcuts import render
from models import Blog


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def get_all_blogs(request):
    blogs = Blog.objects.all()
    template = loader.get_template('blogs.html')
    context = RequestContext(request, {
        'blogs': blogs
    })
    return HttpResponse(template.render(context))


def get_blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(id=blog_id)
    except:
        raise Http404('No existe XD')
    return render(request, 'blog_detail.html', dict(blog=blog))
