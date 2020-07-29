from django.shortcuts import render, HttpResponse


def justtest(request):
    return HttpResponse('Returns GITHUB')


def test(request):
    """ view created for testing the modification 
        it's just a sample view
    """
    return HttpResponse("welcome")


def sathis(request):
    return HttpResponse("I am looking for merg conflicts")

