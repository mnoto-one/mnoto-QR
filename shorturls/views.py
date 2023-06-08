from django.shortcuts import render, redirect
from .models import ShortURL
import random
import string

def shorten_url(request):
    if request.method == 'POST':
        long_url = request.POST.get('long_url')
        short_code = generate_short_code()
        short_url = ShortURL(long_url=long_url, short_code=short_code)
        short_url.save()
        return render(request, 'theme-i/pages/shorturls/shorten.html', {'short_url': short_url})

    return render(request, 'theme-i/pages/shorturls/shorten.html')

def redirect_to_long_url(request, short_code):
    short_url = ShortURL.objects.get(short_code=short_code)
    return redirect(short_url.long_url)

def generate_short_code():
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(6))