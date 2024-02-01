from django.urls import path
from accountapp.views import hello_world

app_name = 'accountapp'
'''
원래는 '127.0.0.1:8000/account/hello_world'라는 주소에 들어감. 그런데 이 긴 주소를 항상 치기는 너무 번거로움.
따라서 accountapp 내부에서 hello_world라는 name을 가진 route로 그대로 가라는 식으로, 'accountapp:hello_world'만 쳐도 이전과 똑같은 주소로 mapping될 수 있는 함수가 있음. 그래서 app_name과 name='hello_world'와 같이 정의하는 것임.
'''

urlpatterns = [
  path('hello_world/', hello_world, name='hello_world')     # views.py에서 hello_world라는 view를 만들었으므로. name은 이 route에 대한 이름임.
]
