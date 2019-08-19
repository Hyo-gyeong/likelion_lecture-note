# def ready():
#     print('우선 일어나')
#     print('밥 먹어')
#     print('씻어')
#     print('출바알') #뒤에 ; 붙이는거 아니야-----

# ready() #함수를 실행하는 코드를 적어줘야 실행결과 나옴.

# def mamma(money):
#     라면 = 3000
#     돈까스 = 5000

#     print('식당으로 고!')
#     print('라면과 돈까스 시킴')
#     print('먹어')
#     print(f'계산해. 여기 {money}원이요')
    
#     잔돈 = money - 라면 - 돈까스
#     return 잔돈

# jandon = mamma(10000) #return 값은 인자가 들어있는 함수가 실행되어야 정해지기때문에 이렇게 정의를 꼭해줘야 밑에서 잔돈을 출력할 수 있음.
# print(f'여기 {jandon}원 남겨왔어용') #위 함수 실행 결과를 jandon이라는 또 다른 변수에 담아주는게 보기 좋음. 안 헷갈림.

# def work ():
#     print('효경아 공부하자')
#     print('아 귀찮아')
#     return ('파이썬 강의')

# lecture = work() #함수의 결과(return이 있을 때)를 변수로 담아와야 사용 가능..!
# print(f'그래서 오늘 뭐공부하는데?? 바로바로 {lecture}')

# number1 = int("100")
# print(number1)

# number2 = float('12.3')
# print(number2)

# year = input("당신의 출생 년도는?")

# age = 2019 - int(year) + 1
# print(f"당신의 나이는 {age}입니다.")

def study_hard(hours):
    print("공부하자 효경아!\n" * hours)
    effects = 10 * hours
    return effects

print(f"{study_hard(10)}만큼의 실력을 쌓았습니다.")