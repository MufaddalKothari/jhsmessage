from datetime import datetime
from django.shortcuts import redirect,render
import pymongo
connect_string = 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.uzyzt.mongodb.net/sample_restaurants?retryWrites=true&w=majority' 
from django.contrib import messages
from django.conf import settings
from .forms import UploadImage
import json
import os
import pathlib
from pathlib import Path
from django.core.files.storage import FileSystemStorage

def handle_uploaded_file(file,route):
    fs = FileSystemStorage(location=route)
    file = fs.save(file.name,file)
    # the fileurl variable now contains the url to the file. This can be used to serve the file when needed.
    fileurl = fs.url(file)
    print(fileurl)

def extract_hashtags(text):
    hashtag_list = []
    for word in text.split():
        if word[0] == '#':
            hashtag_list.append(word)
    return hashtag_list

# Create your views here.
def profile_view(request,email,*args,**kwargs):
    #print(request.session['email'],email)
    #try:
    #    print(request.session['email'],email)
    #    if request.session['email'] != email:
    #        raise PermissionDenied
    #    else:
    connect_string = 'mongodb+srv://m001-student:m001-mongodb-basics@sandbox.uzyzt.mongodb.net/sample_restaurants?retryWrites=true&w=majority' 
    my_client = pymongo.MongoClient(connect_string)
    dbname = my_client.jhsinsta
    collection_name = dbname.users
    count = list(collection_name.find({'email':email}))
    request.session['logged_in'] == True
    variables = {'email':count[0],'id':email[0:5]}
    return render(request,'profile.html',variables)
    #except:
    #    print("Please Login First")
    #    return redirect('http://127.0.0.1:8000/login/')


def newpost_view(request,email,*args,**kwargs):
    id = int(email[0:5])
    tbposts = pymongo.MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.uzyzt.mongodb.net/jhsinsta?retryWrites=true&w=majority').jhsinsta.posts
    row = list(tbposts.find({'email':email}))
    if request.method == 'POST':
        mutable = request.POST._mutable
        request.POST._mutable = True
        request.POST['poster'] = id
        request.POST['hashtags'] = [f['value'] for f in json.loads(request.POST['hashtags'])]
        request.POST['taggedpeeps'] = [f['value'] for f in json.loads(request.POST['taggedpeeps'])]
        request.POST['date'] = datetime.now()
        request.POST._mutable = mutable
        form=UploadImage(request.POST,request.FILES)
        if form.is_valid():
            print(form.cleaned_data)
            path = settings.MEDIA_URL + '/posts/'+str(id)+'/'
            #function to update all this shit into th mongo db database
            handle_uploaded_file(request.FILES['image'],path)
            print('file saved successfully')
            newpost = {
                'user_id':id,
                'image':path+request.FILES['image'].name,
                'date':request.POST['date'],
                'location':request.POST['location'],
                'hashtags':request.POST['hashtags'],
                'taggedpeeps':request.POST['taggedpeeps'],
                'caption':request.POST['caption'],
                'likes':0,
                'comments':[],
                }
            tbposts.insert_one(newpost)
            print(newpost)
        else:
            print('Form is not clean')
        #newpost = {
        #    'date':request.POST['date'],
        #    'location':request.POST['location'],
        #    'hashtags':[f['value'] for f in json.loads(request.POST['tags'])],
        #    'tags':[f['value'] for f in json.loads(request.POST['hashtags'])]
        #    }
        #print(newpost)
        #print(request.FILES['PostedImage'])
    form=UploadImage()
    variables={'id':id,'form':form}
    return render(request,'newpost.html',variables)



def feed_view(request,email,*args,**kwargs):
    id = int(email[0:5])
    
    tbposts = pymongo.MongoClient('mongodb+srv://m001-student:m001-mongodb-basics@sandbox.uzyzt.mongodb.net/jhsinsta?retryWrites=true&w=majority').jhsinsta.posts
    posts = list(tbposts.find())
    print(posts)
    print(posts[1]['image'])
    variables = {'id':id,'posts':posts}
    return render(request,'test.html',variables)