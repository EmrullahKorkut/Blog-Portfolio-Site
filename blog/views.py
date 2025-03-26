from django.shortcuts import get_object_or_404, redirect, render

from blog.models import Blog, Category


def home(request):
    context = {
        'blogs':Blog.objects.filter(favourite=True),
        'categories':Category.objects.all(),
    }
    return render(request, 'blog/home.html', context)




def blog(request):
    context = {
        'blogs': Blog.objects.all(),
        'categories': Category.objects.all()
    }
    return render(request, 'blog/blog.html', context)




def blog_details(request, slug):
    context = {
        'blogs': Blog.objects.get(slug=slug),
        'categories':Category.objects.all(),
    }
    return render(request, 'blog/blog-details.html', context)





def blog_category(request, slug):
    selected_category = get_object_or_404(Category, slug=slug)
    context = {
        "blogs":Blog.objects.filter(categories__slug=slug),
        "categories":Category.objects.all(),
        "selected_category":slug,
        "selected_category_name":selected_category.name
    }

    return render(request, 'blog/blog-list.html', context)





def search(request):
    if "search" in request.GET and request.GET["search"] != "":
        search = request.GET["search"]
        blogs = Blog.objects.filter(title__contains = search).order_by("title")
        categories = Category.objects.all()
    else:
        return redirect("/blog")

    return render(request, 'blog/search.html', 
    {
        'categories': categories,
        'blogs': blogs,
        'search':search,
    })










def about(request):
    context = {
        'blogs': Blog.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'blog/about.html',context)

def contact(request):
    context = {
        'blogs': Blog.objects.all(),
        'categories': Category.objects.all()
    }

    return render(request, 'blog/contact.html',context)