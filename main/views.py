import pytils.translit
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from main.models import student


# Create your views here.
class StudentListView(ListView):
    model = student
    template_name = 'main/index.html'
    extra_context = {'title': 'Главная'}

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class StudentCreateView(CreateView):
    model = student
    fields = ('name', 'description',)
    success_url = reverse_lazy('main:index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = pytils.translit.slugify(new_mat.name)
            new_mat.save()
        return super().form_valid(form)


class StudentUpdateView(UpdateView):
    model = student
    fields = ('name', 'description',)
    success_url = reverse_lazy(f'main:index')

    def form_valid(self, form):
        if form.is_valid():
            new_mat = form.save()
            new_mat.slug = pytils.translit.slugify(new_mat.name)
            new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('main:view', args=[self.kwargs.get('pk')])


class StudentDetailView(DetailView):
    model = student
    extra_context = {'title': 'Материал'}

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.view_count += 1
        self.object.save()
        return self.object


class StudentDeleteView(DeleteView):
    model = student
    success_url = reverse_lazy('main:index')


def contacts(request):
    if (request.method == 'POST'):
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        print(f'Имя: {name} Email: {email} Сообщение: {message}')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'main/contacts.html', context)
