from django.shortcuts import render
from minimum_prices.models import *


# Create your views here.
def minimum_prices_page(request, server_id, ):
    current_server = Server.objects.get()
    mods = Mod.objects.filter(id__in=current_server.items.all().values_list('mod', flat=True))
    print(mods)
    data = {
        'current_server': current_server,
        'mods': mods,
    }
    return render(request, 'minimum_prices_page.html', data)
