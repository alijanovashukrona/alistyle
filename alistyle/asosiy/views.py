from django.shortcuts import render
from django.views import View

class Home(View):
    def get(self,request):
        return render(request,'page-index.html')

class LoginsizHome(View):
    def get(self,request):
        return render(request,'page-index-2.html')
