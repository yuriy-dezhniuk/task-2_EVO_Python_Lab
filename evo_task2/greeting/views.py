from django.shortcuts import render
from .models import FullName
from .forms import FullNameForm


def index(request):
    error = ''
    if request.method == 'POST':
        form = FullNameForm(request.POST)
        if form.is_valid():
            full_names = FullName.objects.all()
            is_name_new = True
            for full_name in full_names:
                if form.instance.first_name == full_name.first_name \
                        and form.instance.last_name == full_name.last_name:
                    is_name_new = False
            if is_name_new:
                greeting_msg = f'Hello, {form.instance.first_name} {form.instance.last_name}!'
                form.save()
            else:
                greeting_msg = f'Already seen, {form.instance.first_name} {form.instance.last_name}!'
            new_form = FullNameForm()
            context = {
                'form': new_form,
                'greeting_msg': greeting_msg,
            }
            return render(request, 'greeting/index.html', context)

        else:
            error = 'Invalid form'
    form = FullNameForm()
    context = {
        'form': form,
        'error': error,
    }
    return render(request, 'greeting/index.html', context)


def name_list(request):
    full_names = FullName.objects.all()
    return render(request, 'greeting/names.html', {'title': 'List of names', 'full_names': full_names})
