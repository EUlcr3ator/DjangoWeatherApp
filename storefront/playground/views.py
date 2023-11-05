from django.shortcuts import render
from django.http import HttpResponse
from pyowm import OWM
# Create your views here.
# request -> response
# request handler
# action

def say_hello(request):
    #owm =OWM('74ed815c713edb5c95dc222916c63dbb')
    #mgr = owm.weather_manager()
    #observation = mgr.weather_at_place("London")
    #w = observation.weather
    #temp = w.temperature('celsius')["temp"]
    #return (HttpResponse("Hello World"))
    return render(request, 'hello.html', {'name': "temp", "weather": "Тест кнопки"})

def weather(request):
    city = request.POST.get("your_city", "Undefined")
    owm =OWM('74ed815c713edb5c95dc222916c63dbb')
    mgr = owm.weather_manager()
    observation = mgr.weather_at_place(city)
    w = observation.weather
    temp = w.temperature('celsius')["temp"]
    humid = w.humidity
    wind = w.wind()
    wind = wind['speed']
    rain = w.rain
    if len(rain) == 0:
        rain = "Дощу немає"
    data = {"city": city, "temp": temp, "humid": humid, "wind": wind, "rain": rain}
    #return HttpResponse(f"<h2>City: {city} Temperature: {temp}</h2>")
    return render(request, 'test.html', context=data)