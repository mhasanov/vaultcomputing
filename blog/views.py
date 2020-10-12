from django.shortcuts import render

posts = [
    {
        'author': 'Mehdi Hasanov',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'October 12, 2020'
    },
    {
        'author': 'Mehdi Hasanov',
        'title': 'Blog Post 2',
        'content': 'First post content',
        'date_posted': 'October 12, 2020'
    }
]

def home(request):
    context = {
            'posts': posts
        }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')
