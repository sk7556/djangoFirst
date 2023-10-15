from django.shortcuts import render

def blog(request):
    return render(request, 'blog/blog.html')

def post(request, pk):
    return render(request, 'blog/post.html')

# 간소화를 위해 blog > templates > blog > blog.html
# 간소화를 위해 blog > templates > blog > post.html