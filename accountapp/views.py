from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from accountapp.models import HelloWorld
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from accountapp.forms import AccountUpdateForm


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
  success_url = reverse_lazy('accountapp:hello_world')    # 계정을 만드는 데 성공했다면 어느 경로로 재연결할 것인가 - 여기서는 accountapp의 hello_world로 재연결하라.
  template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
  model = User
  context_object_name = 'target_user'  # template에서 사용하는 user 객체의 이름을 다르게 설정해줌. 이렇게 하면 다른 사람이 오더라도 나의 페이지를 볼 수 있음 (인스타그램처럼)
  template_name = 'accountapp/detail.html'


class AccountUpdateView(UpdateView):
  model = User
  form_class = AccountUpdateForm
  success_url = reverse_lazy('accountapp:hello_world')  # 계정을 만드는 데 성공했다면 어느 경로로 재연결할 것인가 - 여기서는 accountapp의 hello_world로 재연결하라.
  template_name = 'accountapp/update.html'