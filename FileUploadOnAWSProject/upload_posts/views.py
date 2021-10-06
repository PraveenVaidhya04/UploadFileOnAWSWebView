from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse
from .models import Posts
from .forms import PostsForm
from django.views import generic
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages


@method_decorator(login_required , name="dispatch")
class UploadPostsView(SuccessMessageMixin, generic.CreateView):
    form_class = PostsForm
    template_name = 'upload_posts/create_posts.html'

    def get_success_message(self, cleaned_data):
        return "Posts created."

    def get_context_data(self, *args, **kwargs):
        context = super(UploadPostsView, self).get_context_data(*args, **kwargs)
        return context

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(reverse('upload_posts_app_link:view_own_posts'))

    def form_invalid(self, form):
        messages.error(self.request, form.errors)
        return HttpResponseRedirect(reverse('upload_posts_app_link:upload_posts'))


class ViewPostsView(generic.TemplateView):
    template_name = 'upload_posts/view_posts.html'

    def get_context_data(self, id, *args, **kwargs):
        context = super(ViewPostsView, self).get_context_data(*args, **kwargs)
        context['posts_data'] = get_object_or_404(Posts, id=id)
        return context


@method_decorator(login_required , name="dispatch")
class ViewOwnPostsView(SuccessMessageMixin, generic.ListView):
    model = Posts
    template_name = 'upload_posts/index.html'
    context_object_name = 'posts_data'
    paginate_by = 2
    queryset = None

    def get_context_data(self, *args,**kwargs):
        context = super(ViewOwnPostsView, self).get_context_data(*args, **kwargs)
        return context

    def get_queryset(self,**kwargs):
        get_data = Posts.objects.filter(created_by=self.request.user).order_by("-id")
        return get_data
