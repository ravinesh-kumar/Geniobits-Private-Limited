from django.shortcuts import render, redirect
from django.http import HttpResponse
# from.import views
from django.contrib.auth.models import User,auth
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password
from.models import MainApp
import os
from django.core.files.storage import FileSystemStorage
 



def index(request):
    return render(request ,"MainApp/index.html")

def save(request):
    name=request.POST['name']
    mobile=request.POST['mobile']
    #fetch the image
    filepath = request.FILES['myfile']
    filename = filepath.name #store file name
 
    file_type = os.path.splitext(str(filepath))[1]
 
    if(file_type==".csv"):
        obj = FileSystemStorage() #creating object of FileSystemStorage Class
        k   = obj.save(filename, filepath) # using save(FileName, FilePath) function
        uploaded_file_url = obj.url(k)
        
        k1=MainApp(name=name,mobile=mobile)
        k1.save()
        return redirect("index")
        
    else:
        return HttpResponse("Error! Invalid File")
    

    
    
