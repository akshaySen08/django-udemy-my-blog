from django.shortcuts import render
from datetime import date
from django.http.response import Http404
# Create your views here.

all_posts = [
    {
        "slug": "coding-is-just-new-language",
        "image": "coding.jpg",
        "author": "Akshay Sen",
        "date": date(2021, 12, 31),
        "title": "Post Title",
        "excerpt": "Some excerpt",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            
            
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            
        """ 
    },
    {
        "slug": "its-me-max",
        "image": "max.png",
        "author": "Akshay Sen",
        "date": date(2021, 12, 21),
        "title": "Post Title",
        "excerpt": "Some excerpt",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            
        """ 
    },
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Akshay Sen",
        "date": date(2021, 12, 15),
        "title": "Post Title",
        "excerpt": "Some excerpt",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            
        """ 
    },
    {
        "slug": "woods-and-nature",
        "image": "woods.jpg",
        "author": "Akshay Sen",
        "date": date(2021, 12, 11),
        "title": "Post Title",
        "excerpt": "Some excerpt",
        "content": """
            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            

            Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique, culpa maiores dolore nesciunt cumque
            
        """ 
    }
]

def get_date(post):
    return post['date']

def index(request):
    sorted_posts = sorted(all_posts,key=get_date)
    latest_posts = sorted_posts[-3:] # means we will show only 3 posts

    return render(request, 'blog/index.html', {
        'posts': latest_posts
    })


def posts(request):
    return render(request, 'blog/all-posts.html', {
        'all_posts': all_posts
    })


def post_details(request, slug):
    try:
        selected_post = next(post for post in all_posts if post['slug'] == slug)
        return render(request, 'blog/post-details.html', {
            "post": selected_post 
        })
    except:
        raise Http404()
    # pass