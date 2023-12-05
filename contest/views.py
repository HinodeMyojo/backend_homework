from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContestForm
from .models import Contest


def proposal(request, pk=None):
    # Допишите функцию, чтобы она могла работать как на создание заявки,
    # так и на редактирование.

    if pk is not None:
        instance = get_object_or_404(Contest, pk=pk)
    else:
        instance = None

    form = ContestForm(request.POST or None, instance=instance)
    context = {'form': form}
    if form.is_valid():
        form.save()
    return render(request, 'contest/form.html', context)


def delete_proposal(request, pk):
    # Допишите функцию для удаления заявок.
    instance = get_object_or_404(Contest, pk=pk)
    form = ContestForm(instance=instance)
    context = {'form': form}

    if request.method == 'POST':
        instance.delete()
        return redirect('contest:list')
    return render(request, 'contest/form.html', context)

def proposal_list(request):
    contest_proposals = Contest.objects.order_by('id')
    context = {'contest_proposals': contest_proposals}
    return render(request, 'contest/contest_list.html', context)