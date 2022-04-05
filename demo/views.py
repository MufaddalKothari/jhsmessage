from django.shortcuts import redirect, render
from .forms import NewUser
import json
from django.contrib import messages
# Create your views here.
import pymongo
connect_string = 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.uzyzt.mongodb.net/sample_restaurants?retryWrites=true&w=majority' 
from django.conf import settings

def signup_view(request,*args,**kwargs):
    try:
        login_check = request.session['logged_in'] == True
        email = request.session['email']
        variables = {'email':email[0:5]}
        return redirect('/profile/%s' %request.session['email'],variables)       
    except :
        my_client = pymongo.MongoClient(connect_string)
        dbname = my_client.jhsinsta
        collection_name = dbname.users

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            print(request)
            # create a form instance and populate it with data from the request:
            form = NewUser(request.POST)
            # check whether it's valid:
            if form.is_valid():
                newdude = {
                    '_id':int(form.cleaned_data['email'][0:5]),
                    'email':form.cleaned_data['email'],
                    'password':form.cleaned_data['password']
                    }
                print(newdude)
                count = list(collection_name.find({'email':form.cleaned_data['email']}))
                print(count)
                if count:
                    variables={'form':form}
                    messages.error(request, 'User already exists, Please login')
                    return render(request,'signup.html',variables)
                else:                    
                    collection_name.insert_one(newdude)
                    request.session['logged_in'] = True
                    request.session['email'] = form.cleaned_data['email']
                    messages.success(request, 'Your account has been created')
                    email=request.session['email']
                    variables = {'email':email}
                    return redirect('/profile/%s' %request.session['email'],variables)

# if a GET (or any other method) we'll create a blank form
    form = NewUser()
    variables={'form':form}
    return render(request,'signup.html',variables)




def home_view(request,*args,**kwargs):
    variables = {}
    return render(request,'home.html',variables)


def login_view(request,*args,**kwargs):
    try:
       login_check = request.session['logged_in'] == True
       email=request.session['email'][0:5]
       variables = {'email':email[0:5]}
       return redirect('/profile/%s' %request.session['email'],variables)
    except:
        my_client = pymongo.MongoClient(connect_string)
        dbname = my_client.jhsinsta
        collection_name = dbname.users

        # if this is a POST request we need to process the form data
        if request.method == 'POST':
            print(request)
            # create a form instance and populate it with data from the request:
            form = NewUser(request.POST)
            # check whether it's valid:
            if form.is_valid():
                count = list(collection_name.find({'email':form.cleaned_data['email']}))
                print(count)
                if count:
                    if count[0]['email'] == form.cleaned_data['email'] and count[0]["password"] == form.cleaned_data['password']:
                        request.session['logged_in'] = True
                        request.session['email'] = count[0]['email']
                        messages.error(request, 'Logged In')
                        variables = {'email':request.session['email']}
                        return redirect('/profile/%s' %request.session['email'],variables)
                    else:
                        variables={'form':form}
                        messages.error(request, 'Username and password does not match')
                        return render(request,'login.html',variables)
                else:
                    messages.error(request, 'User does not exist')
                    variables={'form':form}
                    return render(request,'login.html',variables)
    form = NewUser()
    variables = {'form':form}
    return render(request,'login.html',variables)





def logout_view(request,*args,**kwargs):
    request.session.flush()
    variables={}
    return redirect('http://127.0.0.1:8000/')



#def profile(request,email,*args,**kwargs):
#    try:
#        if request.session['email'] != email:
#            raise PermissionDenied
#        else:
#            my_client = pymongo.MongoClient(connect_string)
#            dbname = my_client.jhsinsta
#            collection_name = dbname.users
#            count = list(collection_name.find({'email':email}))
#            request.session['logged_in'] == True
#            variables = {'email':count[0]}
#            return render(request,'profile.html',variables)
#    except:
#        print("Please Login First")
#        return redirect('http://127.0.0.1:8000/login/')
