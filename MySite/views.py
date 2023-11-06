from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import DeleteView, UpdateView
from .forms import *
from .models import Applications, Category
from django.views import generic
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin


# Create your views here.


class ApplicationsView(generic.ListView):
    model = Applications
    template_name = 'index.html'
    context_object_name = 'application'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['num_AcceptedForWork'] = Applications.objects.filter(status__exact='Принято в работу').count()
        return context

    def get_queryset(self):
        return Applications.objects.filter(status__exact='Выполнено').order_by('-date_create')[:4]


class RegistrateUser(CreateView):
    success_url = reverse_lazy('index')
    template_name = 'registration/register.html'
    form_class = RegisterUserForm


class UserLoginView(LoginView):
    template_name = 'registration/login.html'
    success_url = 'index.html'


class applicationByUserListView(LoginRequiredMixin, generic.ListView):
    model = Applications
    template_name = 'MySite/application_list_user.html'
    context_object_name = 'applications'

    def get_queryset(self):
        status = self.request.GET.get('status')
        queryset = Applications.objects.filter(borrower=self.request.user).order_by('-date_create').order_by(
            '-time_create')
        if status:
            queryset = queryset.filter(status=status)
        return queryset


class ApplicationsCreate(LoginRequiredMixin, CreateView):
    model = Applications
    fields = ['title', 'deck', 'category', 'image']
    success_url = reverse_lazy('applicationByUserListView')

    def form_valid(self, form):
        form.instance.borrower = self.request.user
        return super().form_valid(form)


class ApplicationsDelete(DeleteView):
    model = Applications
    success_url = reverse_lazy('applicationByUserListView')
    context_object_name = 'application'


class ApplicationsUpdate(UpdateView):
    model = Applications
    fields = ['title', 'deck', 'category', 'image', 'status']
    success_url = reverse_lazy('applicationByAdminListView')


class applicationByAdminListView(generic.ListView):
    model = Applications
    template_name = 'MySite/application_list_admin.html'
    context_object_name = 'applications'


class createCategory(CreateView):
    model = Category
    fields = ['name']
    success_url = reverse_lazy('applicationByAdminListView')


class CategoryDelete(DeleteView):
    model = Category
    success_url = reverse_lazy('applicationByAdminListView')
    context_object_name = 'CategoryDelete'


class CategoryByAdminListView(generic.ListView):
    model = Category
    template_name = 'MySite/Category_delete.html'
    context_object_name = 'CategoryDeleteList'
