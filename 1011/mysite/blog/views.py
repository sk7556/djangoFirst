from django.shortcuts import render, redirect
from .models import Post

def blog(request):
    db = Post.objects.all()
    context = {
        'db': db,
    }
    return render(request, 'blog/blog.html', context)

def post(request, pk):
    db = Post.objects.get(pk=pk)
    context = {
        'db': db,
    }
    return render(request, 'blog/post.html', context)

def test(request):
    return render(request, 'blog/test.txt')

def posttest(request, pk):
    q = Post.objects.create(title=f'{pk}', contents=f'{pk}{pk}')
    q.save()
    return redirect('blog')































# from django.shortcuts import render
# from django.template.loader import render_to_string
# from django.http import HttpResponse, JsonResponse
# # from django.http import JsonResponse, HttpResponse, HttpResponseRedirect, HttpResponseNotFound, Http404, HttpResponseForbidden

# def blog(request):
#     return render(request, 'blog/blog.html')

# def post(request, pk):
#     return render(request, 'blog/post.html')

# def test(request):
#     data = [
#         {'title': 'Post 1', 'text': 'Text 1', 'pk': 1},
#         {'title': 'Post 2', 'text': 'Text 2', 'pk': 2},
#         {'title': 'Post 3', 'text': 'Text 3', 'pk': 3},
#     ]
#     s = '<h1>{{title}}</h1><p>{{text}}</p>'
    
#     # return HttpResponse('hello world') #1 
#     # return HttpResponse('<h1> Hello World </h1>') #2 
#     # return HttpResponse(s) # 3
#     # return HttpResponse(s.replace('{{title}}',data[0]['title']).replace('{{text}}',data[0]['text'])) # 4
    
#     header = '<h2>hello world</h2>'
#     main = render_to_string('blog/test.txt',{'data' : data[0]})
#     footer = '<p> bye world </p> '
    
#     # return HttpResponse(header + main + footer) # 5
    
#     return JsonResponse(data, safe=False) # 6
    