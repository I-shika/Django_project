from django.shortcuts import render
# from django.http import HttpResponse

posts =  [
      {
        'author': 'ishika',
        'title' : 'blog-post-1',
        'content': 'first post',
        'date' : '23-09-22'
    },
    {
        'author': 'you',
        'title' : 'blog-post-2',
        'content': 'second post',
        'date' : '23-10-22'
    } 

]

def home(request):
    context = {
    'posts' : posts
    }
    return render(request,'blog/home.html', context)
# def about(request):
#     return HttpResponse('<h1>about</h1>')

def about(request):
    return render(request,'blog/about.html',{'title':'about'})


    # for view return type should be httpresponse 
    # render is shortcut method which bydefault returns the value un httpprotocols in background 