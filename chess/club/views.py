from django.shortcuts import render,HttpResponse,redirect
from .models import tournament,player,member,match
from django.core.paginator import Paginator
# Create your views here.

def index(request):
    return render(request,'welcom.html')
def index2(request):
    return render(request,'chosse.html')

def get_tour(request):
    tour = tournament.objects.all()
    return render(request,'show/showtou.html',{'tour':tour})

def get_mem(request):
    mem = member.objects.all()
    return render(request,'show/showmem.html',{'mem':mem})

def get_player(request):
    play = player.objects.all()
    return render(request, 'show/showplay.html', {'play': play})

def get_match(request):
    mat = match.objects.all()
    return  render(request,'show/showmat.html',{'mat':mat})

def gotoin1(request):
    return render(request,'insert/inserttou.html')

def gotoin2(request):
    return render(request,'insert/insertpla.html')

def gotoin3(request):
    return render(request,'insert/insertmem.html')

def gotoin4(request):
    print("asdas")
    return render(request,'insert/insertmat.html')

def inserttou(request):
    id = request.POST['id']
    name = request.POST['name']
    club_id = request.POST['club_id']
    tou = tournament(id,name,club_id)
    tou.save()
    return render(request,'chosse.html')

def insertplay(request):
    id = request.POST['id']
    name = request.POST['name']
    member_id = request.POST['member_id']
    play = player(id,name,member_id)
    play.save()
    return render(request,'chosse.html')

def insertmem(request):
    id = request.POST['id']
    name = request.POST['name']
    club_id = request.POST['club_id']
    mem = member(id,name,club_id)
    mem.save()
    return render(request,'chosse.html')

def insertmat(request):
    id = request.POST['id']
    player_one_id = request.POST['player_one']
    player_two_id = request.POST['player_two']
    winner_id = request.POST['winner']
    tournament_id = request.POST['tour']
    play_date_time = request.POST['play_date_time']
    mat = match(id,player_one_id,player_two_id,winner_id,tournament_id,play_date_time)
    mat.save()
    return render(request,'chosse.html')

def delete(request,id):
    mm = member.objects.get(id=id)
    mm.delete()
    return redirect("/")

def deletetou(request,id):
    mm = tournament.objects.get(id=id)
    mm.delete()
    return redirect("/")

def deletepla(request,id):
    mm = player.objects.get(id=id)
    mm.delete()
    return redirect("/")
def deletemat(request,id):
    mm = match.objects.get(id=id)
    mm.delete()
    return redirect("/")

def update(request,id):
    mm = tournament.objects.get(id=id)
    return render(request,'update/update.html',{'mm':mm})

def uprec(request,id):
    x = request.POST['name']
    mm=tournament.objects.get(id=id)
    mm.name = x
    mm.save()
    return redirect("/")

def updatemem(request,id):
    mm = member.objects.get(id=id)
    return render(request,'update/updatemem.html',{'mm':mm})

def uprecmem(request,id):
    x = request.POST['name']
    mm=member.objects.get(id=id)
    mm.name = x
    mm.save()
    return redirect("/")

def updateplay(request,id):
    mm = player.objects.get(id=id)
    return render(request,'update/updateplay.html',{'mm':mm})

def uprecplay(request,id):
    x = request.POST['name']
    mm=player.objects.get(id=id)
    mm.name = x
    mm.save()
    return redirect("/")