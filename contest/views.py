from typing import Any
from django import http
from django.http.response import HttpResponse
from .forms import ContestForm, CongratulationForm
from .models import Contest, Congratulation
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView, DetailView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.decorators import login_required


class ProporsalMixin:
    model = Contest
    success_url = reverse_lazy('contest:list')

class ProporsalFormMixin:
    template_name = 'contest/form.html'
    form_class = ContestForm

class ProporsalView(ProporsalMixin, ProporsalFormMixin, LoginRequiredMixin, CreateView):
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ProporsalEditView(ProporsalMixin, ProporsalFormMixin, LoginRequiredMixin, UpdateView):
    def dispatch(self, request, *args, **kwargs):
        get_object_or_404(Contest, pk=kwargs['pk'], author=request.user)
        return super().dispatch(request, *args, **kwargs)

class ProporsalDeleteView(ProporsalMixin, LoginRequiredMixin, DeleteView):
    pass

class ProporsalListView(ListView):
    model = Contest
    ordering = 'id'
    paginate_by = 5
    template_name = 'contest/contest_list.html'

class ProporsalDetailView(DetailView):
    model = Contest

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['form'] = CongratulationForm()
        context['congratulations'] = (
            self.object.congratulations.select_related('author')
        )
        return context

@login_required
def add_comment(request, pk):
    obj_of_contest = get_object_or_404(Contest, pk=pk)
    form = CongratulationForm(request.POST)
    if form.is_valid():
        congratulation = form.save(commin=False)
        congratulation.author = request.user
        congratulation.contest = Contest
        congratulation.save()
    return redirect('contest:detail')

#View-функция описанная через функции.

# def proposal(request, pk=None):
#     # Допишите функцию, чтобы она могла работать как на создание заявки,
#     # так и на редактирование.

#     if pk is not None:
#         instance = get_object_or_404(Contest, pk=pk)
#     else:
#         instance = None

#     form = ContestForm(
#         request.POST or None,
#         files=request.FILES or None,
#         instance=instance)
#     context = {'form': form}
#     if form.is_valid():
#         form.save()
#     return render(request, 'contest/form.html', context)

#View-функция описанная через функции.

# def proposal_list(request):
#     contest_proposals = Contest.objects.order_by('id')
#     paginator = Paginator(contest_proposals, 5)
#     page_number = request.GET.get('page')
#     page_obj = paginator.get_page(page_number)
#     context = {'page_obj': page_obj}
#     return render(request, 'contest/contest_list.html', context)


# def delete_proposal(request, pk):
#     # Допишите функцию для удаления заявок.
#     instance = get_object_or_404(Contest, pk=pk)
#     form = ContestForm(instance=instance)
#     context = {'form': form}

#     if request.method == 'POST':
#         instance.delete()
#         return redirect('contest:list')
#     return render(request, 'contest/form.html', context)
