from django.shortcuts import render, HttpResponse

# Create your views here.


def justtest(request):
    return HttpResponse('Returns GITHUB')