import openai
import os

from .forms import PromptForm
from django.conf import settings

def get_prompt_from_request(request):
    prompt = ''
    if request.method == 'POST':
        form = PromptForm(request.POST)
        if form.is_valid():
            prompt = form.cleaned_data['prompt']
        return prompt
    else:
        return prompt

def get_image_from_api(prompt):
    openai.api_key = settings.OPENAI_API_KEY
    response = openai.Image.create(
        prompt=prompt,
        n=2,
        size='512x512'
    )
    return response['data'][0]['url']
