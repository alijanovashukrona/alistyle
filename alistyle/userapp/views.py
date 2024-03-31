from django.shortcuts import render
from django.views import View
# from eskiz.client import SMSClient
from django.contrib.auth import logout,login,authenticate

class LoginView(View):
    def get(self,request):
        return render(request,'page-user-login.html')

    def post(self,request):
        pass


class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/user/login/')
