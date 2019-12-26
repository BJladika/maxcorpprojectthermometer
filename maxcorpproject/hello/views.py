from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import telebot;
import requests;
import json;
#bot = telebot.TeleBot('959846602:AAEMumNs6tSy1A2tXtGA5pAmCISMM_KECdM	');

# Create your views here.

def index(request):
	# your API key will come here
	appid = '4ead6ad7444e30854bfb5513485cd259'
	s_city = "Yakutsk,ru"
	city_id = 2013159

	infotemp = {
	"conditions:": "No condition",
	"temp:": "No temp",
	"temp_min:": "No temp min",
	"temp_max:": "No temp max",
	}
	try:
			res = requests.get("http://api.openweathermap.org/data/2.5/weather",
				 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
			data = res.json()
			print("conditions:", data['weather'][0]['description'])
			print("temp:", data['main']['temp'])
			print("temp_min:", data['main']['temp_min'])
			print("temp_max:", data['main']['temp_max'])
			infotemp = {
				"conditions": str(data['weather'][0]['description']),
				"temp": str(data['main']['temp']),
				"temp_min": str(data['main']['temp_min']),
				"temp_max": str(data['main']['temp_max']),
			}
			print(infotemp)
			#return render(request, "index.html", args)


	except Exception as e:
			print("Exception (weather):", data)
			infotemp = {
				"conditions:": str(data),
			}
			pass
	args={
		'conditions': infotemp,
		'max-god': "false",
		'dima-cool':{
			'strange': "true",
		}
	}
	return render(request, "index.html", infotemp)


def db(request):

	greeting = Greeting()
	greeting.save()

	greetings = Greeting.objects.all()

	return render(request, "db.html", {"greetings": greetings})

#@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	r = requests.get('https://api.telegram.org/bot959846602:AAEMumNs6tSy1A2tXtGA5pAmCISMM_KECdM/getUpdates')
	return HttpResponse('UPDATES:' + str(r.content))

def test_temperature():
	appid = '4ead6ad7444e30854bfb5513485cd259'
	s_city = "Yakutsk,ru"
	city_id = 2013159

	infotemp = {}
	try:
			res = requests.get("http://api.openweathermap.org/data/2.5/weather",
				 params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
			data = res.json()
			print("conditions:", data['weather'][0]['description'])
			print("temp:", data['main']['temp'])
			print("temp_min:", data['main']['temp_min'])
			print("temp_max:", data['main']['temp_max'])
			infotemp = {
				"conditions:": str(data['weather'][0]['description']),
				"temp:": str(data['main']['temp']),
				"temp_min:": str(data['main']['temp_min']),
				"temp_max:": str(data['main']['temp_max']),
			}


	except Exception as e:
			print("Exception (weather):", data)
			infotemp = {
				"conditions:": str(data),
			}
			pass
	return render_template('index.html', data = infotemp)
