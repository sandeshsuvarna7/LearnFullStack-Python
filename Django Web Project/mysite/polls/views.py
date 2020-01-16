from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You are at the polls index.")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s." %question_id)

def results(request, question_id):
    repsonse = "You are looking ar the results of questions %s."
    return HttpResponse(repsonse % question_id)

def vote(request, question_id):
    return HttpResponse("You are voting on question %s." %question_id)