# Create your views here.
#coding: utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.contrib import auth
from django.core.context_processors import csrf
from form import MyRegistrationForm
from trac_nghiem.models import trac_nghiem
import random
def login(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('login.html',c)
def auth_view(request):
    username= request.POST.get('email','')
    password= request.POST.get('password','')
    user = auth.authenticate(username=username,password=password)
    if (user is not None):
        auth.login(request,user)
        return HttpResponseRedirect('/account/loggedin')
    else:
        return HttpResponseRedirect('/account/invalid')

def loggedin(request):
    return render_to_response('loggedin.html',{'user':request.user.username})
def invalid_login(request):
    return render_to_response('invalid_login.html')
def logout(request):
    del request.COOKIES['sessionid']
    del request.COOKIES['csrftoken']
    return render_to_response('logout.html')
def register_user(request):
    if request.method == 'POST':
        form = MyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/account/register_success')
        else:
            return render_to_response('error.html')
    args = {}
    args.update(csrf(request))
    args['form'] = MyRegistrationForm()
    return render_to_response('register.html',args)
def register_success(request):
    return render_to_response('register_success.html')




def createQuestion(request):
    # tạo form cho người dùng tạo câu hỏi
    c = {}
    c.update(csrf(request))
    return render_to_response('create_question.html',c)

def writeQuestionToDatabase(request):
    '''ghi cau hoi vao trong co so du lieu'''

    if request.method=="POST":
        noi_dung = request.POST.get('noi_dung')
        dap_an_1 = request.POST.get('dap_an_A')
        dap_an_2 = request.POST.get('dap_an_B')
        dap_an_3 = request.POST.get('dap_an_C')
        dap_an_4 = request.POST.get('dap_an_D')
        li = [dap_an_1,dap_an_2,dap_an_3,dap_an_4]
        dap_an_dung = request.POST.get('dap_an_dung')
        giai_thich = request.POST.get('giai_thich')
        temp = trac_nghiem(noi_dung_cau_hoi=noi_dung,dap_an_1=dap_an_1,dap_an_2=dap_an_2,dap_an_3=dap_an_3,dap_an_4=dap_an_4,dap_an_dung=dap_an_dung,giai_thich=giai_thich)
        temp.save()
        return render_to_response('temp.html',{'cau_hoi':noi_dung,'dap_an':dap_an_dung,'cau_tra_loi':li})
def question(request):
    '''tạo ra câu hỏi cho người dùng trả lời từ cơ sở dữ liệu'''
    c = {}
    c.update(csrf(request))
    so_luong_ban_ghi = trac_nghiem.objects.count()
    obj = trac_nghiem.objects.get(ma_cau_hoi=random.randrange(1,so_luong_ban_ghi+1))
    li = [obj.dap_an_1, obj.dap_an_2, obj.dap_an_3, obj.dap_an_4]

    return render_to_response('question.html',{'cau_hoi':obj.noi_dung_cau_hoi,'danh_sach_dap_an':li})
