from django.shortcuts import render

# 언제, 어떤 상황에서 데이처를 처리할 지를 알려주는 python파일, 이 안에 함수를 정의

def home(request): # home이라는 함수에 request가 들어오면
    return render(request, 'home.html') #home 이라고 하는 html 파일을 return해줘 = 갖다줘