from django.shortcuts import render
from .utils import get_prompt_from_request, get_image_from_api
from .forms import PromptForm
# Create your views here.

def index(request):
    return render(request, 'dalle/home.html')

def dalle(request, prompt=''):
    prompt = get_prompt_from_request(request)
    if prompt:
        img = get_image_from_api(prompt)
    else:
        img=''

    context = {
        'form': PromptForm(),
        'img': img
    }
    return render(request, 'dalle/dalle.html', context)

def help(request):
    return render(request, 'dalle/help.html')

def error_404(request, exception):
    return render(request, 'dalle/404.html', status=404)