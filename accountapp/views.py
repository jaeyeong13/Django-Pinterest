from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def hello_world(request):
  if request.method == 'POST':
    temp = request.POST.get('hello_world_input')    # POST method 중에서 hello_world_input이라는 이름을 가진 데이터를 가져와라.
    new_hello_world = HelloWorld()    # HelloWorld 뒤에 괄호를 넣어 주면, HelloWorld라는 빵틀에서 나온 새로운 객체가 new_hello_world라는 변수에 저장이 됨
    new_hello_world.text = temp
    new_hello_world.save()    # 이렇게 하면 실제로 DB에 HelloWorld 객체를 저장하게 됨.

    hello_world_list = HelloWorld.objects.all()     # HelloWorld라는 객체에서 모든 데이터를 긁어옴
    return HttpResponseRedirect(reverse('accountapp:hello_world'))      # accountapp 내부에 있는 hello_world로 재접속하라
  else:
    hello_world_list = HelloWorld.objects.all()
    return render(request, 'accountapp/hello_world.html', context={'hello_world_list':hello_world_list})


class AccountCreateView(CreateView):
  model = User
  form_class = UserCreationForm
  success_url = reverse_lazy('accountapp:hello_world')
  template_name = 'accountapp/create.html'
