from django.shortcuts import render
from urlbox import UrlboxClient
from django.core.files.base import ContentFile
from decouple import config
from .models import Screenshot


API_KEY = config('API_KEY')
SECRET_KEY = config('SECRET_KEY')


def index(request):
    if request.method == 'POST':
        user_url = request.POST['url']
        client = UrlboxClient(api_key=API_KEY, api_secret=SECRET_KEY)
        response = client.get({'url': user_url, 'full_page': True, 'block_ads': True})
        file = ContentFile(response.content)
        screenshot = Screenshot(url=user_url)
        screenshot.photo.save('image.png', file)
        context = {
            'img': screenshot
        }
        return render(request, 'index.html', context)
    return render(request, 'index.html')

