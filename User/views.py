<<<<<<< Updated upstream
from django.http import HttpResponse


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
=======
from django.shortcuts import render
# Create your views here.

def login(request):

    return render(
        request,
        'User/login.html')
def logout(request):

    return render(
        request,
        'User/logout.html')
        
>>>>>>> Stashed changes
