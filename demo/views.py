import datetime
import random
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from demo.models import Car, Person, Order, Product, OrderPosition, Weapon
from .serializers import WeaponSerializers

# Create your views here.
@api_view(['GET', 'POST'])
def msg(request):
    if request.method == 'GET':
        weapons = Weapon.objects.all()
        ser = WeaponSerializers(weapons, many=True)
        data = {'message': 'Hello'}
        return Response(ser.data)
    if request.method == 'POST':
        return Response({'status': 'Ok'})
        pass

class DemoView(APIView):
    def get(self, request):
        if request.method == 'GET':
            weapons = Weapon.objects.all()
            ser = WeaponSerializers(weapons, many=True)
            return Response(ser.data)
    def post(self, request):
        return Response({'status': 'Ok'})


def list_orders(request):
    orders = Order.objects.all()
    context = {'orders': orders}
    return render(request, 'orders.html', context)
def list_person(request):
    person_objects = Person.objects.all()
    people = [f'{p.name}: {p.car}' for p in person_objects]
    # people = [f'{p.name}: {p.car.brand}, {p.car.model}, {p.car.color}' for p in person_objects]
    return HttpResponse('<br>'.join(people))
def create_person(request):
    cars = Car.objects.all()
    for car in cars:
        # Person(name='P', car=car).save()
        Person.objects.create(name='P', car=car)
    return HttpResponse('Good!')
def list_car(request):
    car_objects = Car.objects.all()
    car_objects = Car.objects.filter(brand="B1")
    car_objects = Car.objects.filter(brand__contains='2')
    car_objects = Car.objects.filter(brand__startswith='B')
    cars = [f'{c.id}: {c.brand}, {c.model}: {c.color} | {c.owners.count()}' for c in car_objects]
    return HttpResponse('<br>'.join(cars))
def create_car(request):
    car = Car(
        brand=random.choice(['B1', 'B2', 'B3']),
        model=random.choice(['M1', 'M2', 'demo']),
        color=random.choice(['C1', 'C2', 'demo'])
    )
    car.save()
    return HttpResponse(f'Good! New car: {car.brand}, {car.model}, {car.color}')
def pagi(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(CONTENT, 10)
    page = paginator.get_page(page_number)
    context = {
        'page' : page

    }
    return render(request, 'pagi.html', context)

CONTENT = [str(i) for i in range(10000)]
def index(request):
    return HttpResponse('django')

def time(request):
    return HttpResponse(f'Time = {datetime.datetime.now().time()}')

def hello(request):
    name = request.GET.get("name")
    age = int(request.GET.get("age", 20))
    print(age)
    return HttpResponse(f'Hello, {name}')

def sum(request, a, b):
    result = int(a) + int(b)
    return HttpResponse(f'Sum = {result}')

def demo(request):
    context = {
        'test' : 5,
        'data': [1, 5, 8],
        'val': 'Hello'
    }
    return render(request, 'demo.html', context)