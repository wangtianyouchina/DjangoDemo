from django.shortcuts import render
from django.http import *
from .models import  *
#引用html相关的包
# from django.template import RequestContext,loader

def index(request):
    # temp = loader.get_template('booktest/index.html')

    # return HttpResponse(temp.render())
    bookList = BookInfo.objects.all()
    context = {'list':bookList}
    return render(request,'booktest/index.html',context)

def show(request,id):

    booinfo = BookInfo.objects.get(pk=id)
    list = booinfo.heroinfo_set.all()

    context = {'list':list}
    return render(request,'booktest/show.html',context)