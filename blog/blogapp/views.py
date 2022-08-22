from django.shortcuts import render
from django.http import HttpResponse
from blogapp.models import Post


# Create your views here.
# p = Post.objects.filter(title="Tasty Beef Quesadilla from Cilantro Taqueria").get()
# print(p.title)
# print(type(p.title))
# print(f'The title is {p.title}')
from django.shortcuts import render


def detail(request):
    p = Post.objects.filter(title="Tasty Beef Quesadilla from Cilantro Taqueria").get()
    print(Post.objects.filter(title="Tasty Beef Quesadilla from Cilantro Taqueria"))
    return HttpResponse(f'The titldsfzge is {p.title}')

def post(request):
    post_object = Post.objects.filter(title="Tasty Beef Quesadilla from Cilantro Taqueria").get()
    
    return render(request, 'blogapp/post.html', {'post': post_object})