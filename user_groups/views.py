from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView
from .models import CustomUser, CustomGroup
from . import forms
from django.http import Http404
from django.contrib.auth.mixins import LoginRequiredMixin

def index_page(request):
    return render(request, "home.html")


class CustomUserListView(ListView):
    model = CustomUser
    template_name = 'user_list.html'
    context_name = 'user_list'


class CustomGroupListView(ListView):
    model = CustomGroup
    template_name = 'group_list.html'
    context_name = 'group_list'


class CustomUserCreateView(LoginRequiredMixin, CreateView):
    form_class =  forms.CustomUserCreationForm
    success_url = reverse_lazy('user_list')
    template_name = 'user_create.html'


class CustomUserUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomUser
    success_url = reverse_lazy('user_list')
    form_class = forms.CustomUserChangeForm
    template_name = 'user_update.html'


class CustomUserDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomUser
    template_name = 'user_confirm_delete.html'
    success_url = reverse_lazy('user_list')

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        if request.user == user:
            return render(request, 'user_cannot_delete.html')
        return super().get(request, *args, **kwargs)
    

class CustomGroupCreateView(LoginRequiredMixin, CreateView):
    model = CustomGroup
    form_class = forms.CustomGroupForm
    template_name = 'group_create.html'
    success_url = reverse_lazy('group_list')


class CustomGroupUpdateView(LoginRequiredMixin, UpdateView):
    model = CustomGroup
    form_class = forms.CustomGroupForm
    template_name = 'group_update.html'
    success_url = reverse_lazy('group_list')


class CustomGroupDeleteView(LoginRequiredMixin, DeleteView):
    model = CustomGroup
    template_name = 'group_confirm_delete.html'
    success_url = reverse_lazy('group_list')

    def get(self, request, *args, **kwargs):
        group = self.get_object()
        if group.customuser_set.filter(id=request.user.id).exists():
            return render(request, 'group_cannot_delete.html')
        return super().get(request, *args, **kwargs)

