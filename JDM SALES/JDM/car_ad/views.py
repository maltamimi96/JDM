from django.shortcuts import render


# Create your views here.
def car_new(request):
    return render(request,'car_ad/new_car.html')