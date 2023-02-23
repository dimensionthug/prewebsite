from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request, 'index.html')


def count(request):
    return render(request, 'Count.html')

def fungames(request):
    return render(request, 'fungames.html')

def counting(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    return render(request, 'counting.html', {"fulltext":fulltext, "count": len(wordlist)})
