from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import User
from django.shortcuts import HttpResponse
# Create your views here.
# 这两个是普通路由，执行这个方法就会直接到到相应的模板中，写成了函数形式
def regist(request):
    return render(request,"login/regist.html")

def login(requst):
    return render(requst,"login/login.html")
#下面三个都和用户有关，封装成UserController这个类，
class UserController:
    def userLogin(request):
        if request.method == 'POST':
            user_name = request.POST.get("user_name")
            password = request.POST.get("password")
            user = User.objects.get(user_name=user_name)
            if user.password != password :
                return HttpResponse("密码错误")
        return render(request,"login/userinfo.html",{'user':user})

    def userRegist(request):
        if request.method == 'POST':
            user_name = request.POST.get("user_name")
            password = request.POST.get("password")
            age = request.POST.get("age")
            User.objects.create(user_name=user_name, password=password, age=age)
        return render(request, "login/login.html")

    def userInfo(request,id):
        user = User.objects.get(id=id)
        return render(request, "login/userinfo.html", {'user': user})
