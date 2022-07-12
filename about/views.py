import datetime

from django.shortcuts import render

# Create your views here.


def whoami(request):

    contex = {'user_agent': request.META.get('HTTP_USER_AGENT', ''),
              'ip_address': request.META.get('REMOTE_ADDR', ''),
              'server_time': datetime.datetime.now().strftime('%A %B, %d %Y %H:%M:%S'),
              }

    return render(request, 'about/whoami.html', contex)
