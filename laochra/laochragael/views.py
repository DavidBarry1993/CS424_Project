from django.shortcuts import render
from laochragael.models import Player
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth.decorators import login_required

from django.urls import reverse

from laochragael.forms import PlayerForm





# Create your views here.


def player_info(request,member_number):
    m = Player.objects.get(id=member_number)
    response = render(request, 'laochragael/player_detail.html', { 'm' : m })
    return response


def player_list(request):
    l = Player.objects.all()
    response = render(request, 'laochragael/player_list.html', { 'list' : l })
    return response


@login_required
def player_update(request,member_number):
    if request.user.is_authenticated:
        m = Player.objects.get(id=member_number)
        if request.method=="POST":
            form = PlayerForm(request.POST, instance=m)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse('player_profile',kwargs={'member_number':member_number}))
            else:
                return HttpResponseRedirect('/')
        
        form = PlayerForm(instance=m)
        return render(request, 'laochragael/player_update.html',{'form' : form})
    else:
        return render(request, 'laochragael/error.html')
    
