#view.py라는 python파일을 가져와서 연결해줘야함 어떤 url로써 보여줄껀지!
from django.contrib import admin
from django.urls import path
import myapp.views #myapp이라는 폴더안에있는 views.py를 갖고와주세요 왜냐면 그 안에 내가 쓰고싶은 함수가 있으니까요..


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', myapp.views.home, name="home"), #''<-이런 조건일 때 myapp안에 있는 views파일 안에있는 home이라고하는 함수를 실행시켜라(이 home이라는 함수는 home.html을 보여주는 함수 따라서 home.html이 실행됨). 경로이름은 home이라고 할래
]
