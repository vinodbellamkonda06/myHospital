from django.shortcuts import render, HttpResponse


def test(request):
    """ view created for testing the modification 
        it's just a sample view
    """
    return HttpResponse("welcome")
