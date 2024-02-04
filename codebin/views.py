from ssl import AlertDescription
from django.shortcuts import render

# Create your views here.
# view

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from codebin.models import Codebin
import uuid

def index(request):
    if request.method == 'POST':
        pastetitle = request.POST.get('pastetitle')
        pastecontent = request.POST.get('pastecontent')

        # uid for the paste
        pasteID = str(uuid.uuid4().int & (1 << 31) - 1)

        connect = Codebin(pastetitle=pastetitle, pastecontent=pastecontent, sid=pasteID)
        connect.save()

        # Display a success message
        message = f'Paste Created, and your ID is {pasteID}'

        return render(request, 'index.html', {'message': message})

    return render(request, 'index.html')



def find(request):
    if request.method == 'POST':
        pasteID = request.POST.get('pasteID')

        if not pasteID:
            message = 'Enter Paste ID'
            return render(request, 'find.html', {'message': message})

        # Query the database to find the paste with the given ID and visibility
        try:
            paste = Codebin.objects.get(sid=pasteID) 
        except Codebin.DoesNotExist:
            paste = None
        if paste==None:
            message = 'Invalid Paste ID'
            return render(request, 'find.html', {'message': message})
        else:

            return render(request, 'find.html', {'paste': paste})

    return render(request, 'find.html')


def about(request):
    return render(request,'about.html')

def privacy(request):
    return render(request,'privacy.html')




