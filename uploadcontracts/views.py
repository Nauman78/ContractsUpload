import os
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def index(request):
    return render(request, 'index.html')


def upload_file(request):
    folder = 'uploads/'
    if request.method == 'POST':
        myfile = request.FILES['file']
        extension = myfile.name.split(".")[1].lower()
        if(extension == 'pdf' or extension == 'txt' or extension == 'doc'):
            fs = FileSystemStorage(location=folder)
            fs.save(myfile.name, myfile)
            file_url = fs.url(myfile.name)
            return render(request, 'index.html', {
                'file_url': file_url
            })
        else:
            return render(request, 'index.html')



