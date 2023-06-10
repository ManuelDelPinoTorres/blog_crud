from django.shortcuts import render
from django.views.generic.base import View


class BlogListView(View):
    def get(self,request,*args,**kargs):
        context={
            
        }
        return render(request,'blog_list.html',context)

