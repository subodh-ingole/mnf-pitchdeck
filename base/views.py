from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render


rooms = [
	{
		"id":1, "name": "Chat room"
	},
	{
		"id":2, "name": "Web Development room"
	},
	{
		"id":3, "name": "Sleeping room"
	},
]



def home(request):
  return render(request,'base/home.html',{"rooms":rooms})

def room(request,pk):
	var = None
	for room in rooms:
		if room['id'] == int(pk):
			var = room
			
	print(var)
	context = {"room":var}
	return render(request,'base/room.html',context)


character_list = [ "adam", "eve", "soemthing"]


def mnf(request):
	context = {"character_list":character_list}
	return render(request,'base/mnf.html',context)

def character(request):
	print(request.POST.getlist('character_check'))
	return render(request,'base/character.html')
	