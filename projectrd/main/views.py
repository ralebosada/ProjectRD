from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello! Welcome to ProjectRD")

def about(request):
    return HttpResponse("ProjectRD deploys DSP solutions to everyday problems")

def services(request):
    return HttpResponse("These are the solutions currently offered by our project")

def ticket(request, question):
    return HttpResponse("Ticket Request for: %s", % question)

