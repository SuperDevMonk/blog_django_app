from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.contrib.auth.models import User
from django.db.models import Count


def index(request):
    ''' Views the Homepage. '''
    # Gets all the blogs by all the users
    blogs_list = Blog.objects.order_by('-publish_date')

    # Gets the top 5 visited/Liked posts - INCOMPLETE
    blogs_list_top5 = blogs_list[:5]

    # Gets the top 5 authors/contributors
    top_authors = Blog.objects.all().values('author').annotate(
        total=Count('author')).order_by('-total')[:5]
    # List to store the top 5 authors usernames
    authors_list = []
    # Iterating over the top 5 authors queryset and extracting their usernames
    for i in top_authors:
        authors_list.append(User.objects.filter(
            id=i['author']).first().username)

    title = 'Home'
    context = {
        'blogs_list': blogs_list,
        'title': title,
        'blogs_list_top5': blogs_list_top5,
        'top_authors': authors_list,
    }
    return render(request, 'blogs/index.html', context)


def create_post(request):
    # Passes the title of the webpage to the base.html file
    title = 'Create New Post'
    return render(request, 'blogs/create_post.html', {'title': title})