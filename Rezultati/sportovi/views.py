from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy 
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from sportovi.models import *
from django.db.models import Q


def homepage(request):
    return render(request, 'homepage.html')



class SportoviListView(ListView):
    model = Sport
    context_object_name = 'sportovi'
    template_name = 'glavni/sportovi_list.html'


class CreateSport(CreateView):
    model = Sport
    form_class = SportForm
    template_name = 'CRUD/create_sport.html'
    success_url = reverse_lazy('sportovi:sportovi_list')


class UpdateSport(UpdateView):
    model = Sport
    form_class = SportForm
    template_name = 'CRUD/update_sport.html'
    success_url = reverse_lazy('sportovi:sportovi_list')


class DeleteSport(DeleteView):
    model = Sport
    template_name = 'CRUD/delete_sport.html'
    success_url = reverse_lazy('sportovi:sportovi_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sportovi'] = self.get_object()
        return context



class NatjecanjeListView(ListView):
    model = Natjecanje
    context_object_name = 'natjecanja'
    template_name = 'glavni/natjecanje_list.html'

    def get_queryset(self):
        sport_pk = self.kwargs.get('sport_pk')
        if sport_pk:
            return Natjecanje.objects.filter(sport__pk=sport_pk)
        
        return Natjecanje.objects.all()


class  CreateNatjecanje(CreateView):
    model = Natjecanje
    form_class = NatjecanjeForm
    template_name = 'CRUD/create_natjecanje.html'
    success_url = reverse_lazy('sportovi:natjecanje_list')


class UpdateNatjecanje(UpdateView):
    model = Natjecanje
    form_class = NatjecanjeForm
    template_name = 'CRUD/update_natjecanje.html'
    success_url = reverse_lazy('sportovi:natjecanje_list')


class DeleteNatjecanje(DeleteView):
    model = Natjecanje
    template_name = 'CRUD/delete_natjecanje.html'
    success_url = reverse_lazy('sportovi:natjecanje_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sportovi'] = self.get_object()
        return context



class TimListView(ListView):
    model = Tim
    context_object_name = 'timovi'
    template_name = 'glavni/tim_list.html'

    def get_queryset(self):
        natjecanje_pk = self.kwargs.get('natjecanje_pk')
        if natjecanje_pk:
            return Tim.objects.filter(natjecanje__pk=natjecanje_pk)

        return Tim.objects.all()

class CreateTim(CreateView):
    model = Tim
    form_class = TimForm
    template_name = 'CRUD/create_tim.html'
    success_url = reverse_lazy('sportovi:tim_list')


class UpdateTim(UpdateView):
    model = Tim
    form_class = TimForm
    template_name = 'CRUD/update_tim.html'
    success_url = reverse_lazy('sportovi:tim_list')


class DeleteTim(DeleteView):
    model = Tim
    template_name = 'CRUD/delete_tim.html'
    success_url = reverse_lazy('sportovi:tim_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sportovi'] = self.get_object()
        return context



class RezultatUtakmiceListView(ListView):
    model = RezultatUtakmice
    context_object_name = 'rezultati'
    template_name = 'glavni/rezultat_utakmice_list.html'

    def get_queryset(self):
        tim_pk = self.kwargs.get('tim_pk')
        if tim_pk:
            return RezultatUtakmice.objects.filter(Q(domacin__pk=tim_pk) | Q(gost__pk=tim_pk))
        else:
            return RezultatUtakmice.objects.all()  


class CreateUtakmica(CreateView):
    model = RezultatUtakmice
    form_class = RezultatUtakmiceForm
    template_name = 'CRUD/create_utakmica.html'
    success_url = reverse_lazy('sportovi:rezultati_timova')


class UpdateUtakmica(UpdateView):
    model = RezultatUtakmice
    form_class = RezultatUtakmiceForm
    template_name = 'CRUD/update_utakmica.html'
    success_url = reverse_lazy('sportovi:rezultati_timova')
    
    
class DeleteUtakimca(DeleteView):
    model = RezultatUtakmice
    template_name = 'CRUD/delete_utakmica.html'
    success_url = reverse_lazy('sportovi:rezultati_timova')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sportovi'] = self.get_object()
        return context



def user_signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sportovi:login')
    else:
        form = UserCreationForm()
    return render(request, 'registracija/signup.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)    
                return redirect('sportovi:homepage')
    else:
        form = LoginForm()
    return render(request, 'registracija/login.html', {'form': form})


def user_logout(request):
    logout(request)
    return redirect('sportovi:homepage')