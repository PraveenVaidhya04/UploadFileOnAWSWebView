from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.views import generic
from django.contrib import messages
from django.urls import reverse


class AccountRegistrationView(generic.View):
    user_form = SignUpForm

    def get(self,request):
        return render(request,"accounts/registration.html", {"user_form":self.user_form})

    def post(self, request):
        post_data = request.POST or None

        user_form = self.user_form(post_data)
        if user_form.is_valid():
            new_user = user_form.save()
            messages.info(request, 'A Verification code has been sent to your email id. :- ' + new_user.email)
            return HttpResponseRedirect(reverse('home_app_link:home'))
        else:
            messages.error(request, user_form.errors)
        return HttpResponseRedirect(reverse('accounts_app_link:account_login'))
