# Create your views here.
# Create your views here.
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from forms import PostForm
from models import Post

    

@login_required
def new_post(request):
    form = PostForm()
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save(request.user)
            return HttpResponseRedirect(reverse('core.views.list_post'))
    return render_to_response('new_post.html',
            locals(), context_instance=RequestContext(request)
    )

def list_posts(request):
    posts = Post.objects.all()
    return render_to_response('list_posts.html',
            locals(), context_instance=RequestContext(request)
    )

def update_post(request):
    #post = Post.objects.get(pk='5066549580791808')#(request.GET.get('pid')))
    #return render_to_response('update_post.html',
     #       locals(), context_instance=RequestContext(request)
    #html = "<html><body>In %s hour(s), it will be .</body></html>" % request.GET.get('pid')
    #eturn HttpResponse(html)
   # page = Post.objects.get(pk="5066549580791808")
   #content = page.content
    post = Post.object.get(pk='5066549580791808')

    return render_to_response('update_post.html',
            locals(), {"content": post}
    )
       
     



#def new_post(request):
#    form = PostForm()
#    if request.method == 'POST':
#       form = PostForm(request.POST)
#        if form.is_valid():
#            form.save(request.user)
#            return HttpResponseRedirect(reverse('core.views.list_posts'))
#    else:
#        return  render_to_response('new_post.html',
 #           locals(), context_instance=RequestContext(request)
#    )

#def list_posts(request):
#    posts = Post.objects.all()
#    return render_to_response('list_posts.html',
#            locals(), context_instance=RequestContext(request)
#   )

#def list_posts(request):
 #   #action = request.POST.get('UpdateBlog')
  #  if action: #== 'Delete':
  #          return render_to_response('new_post.html',
  ## #else:
   #  #       posts = Post.objects.all()
   #   #      return render_to_response('list_posts.html',
   #    #     locals(), context_instance=RequestContext(request)
   # )
   # else:
   #     return render_to_response('list_posts.html',
   #     locals(), context_instance=RequestContext(request)
   # )