# 함수
# 기본구조
'''

def 함수이름(전달값1, 전달값2, ...):
    실행 명령문1
    실행 명령문2
    ....
    return 반환값1, 반환값2, ...
'''

def deposit(balance,money): #입금
    balance += money # 잔액에 돈을 입금한다
    print("{0}원이 입금완료되었습니다. 잔액은 {1}원입니다.".format(money, balance))
    return balance # 잔액
def withdraw(balance,money): #출금
    commission=100 # 수수료
    if balance+commission<money: # 잔액보다 출금금액이 클 경우
        print("잔액을 초과하였습니다. 출금이 불가능합니다.")
        return money, balance, commission
    else: # 잔액보다 출금금액이 작을  경우
        print("{0}를 출금하였습니다. 남은 금액은 {1}입니다.".format(money, balance-money-100))
        return money, balance-money-100, commission

balance =0 # 초기 자본 0원
balance = deposit(balance, 1000) # 1000원입금
balance = deposit(balance, 1000) # 1000원입금
money,balance,commission=withdraw(balance,500) # 튜플 형식으로 반환된다.
print("{0}의 출금결과.{1}금액 남았습니다. 수수료는 {2}입니다.".format(money, balance, commission))

'''
1000원이 입금완료되었습니다. 잔액은 1000원입니다.
1000원이 입금완료되었습니다. 잔액은 2000원입니다.
500를 출금하였습니다. 남은 금액은 1400입니다.
500의 출금결과.1400금액 남았습니다. 수수료는 100입니다.
'''

#기본값

def profile(name, age, main_language):
    print("{0} 은 나이가 {1}이고 주요 언어는 {2}입니다." .format(name, age, main_language))

profile("김찬영", 29, "python")
#김찬영 은 나이가 29이고 주요 언어는 python입니다.

# 만약 age와 main_language가 기본값이 설정되있다면?
def profile(name, age=18, main_language = "python"):
    print("{0} 은 나이가 {1}이고 주요 언어는 {2}입니다." .format(name, age, main_language))

profile("김도규")
profile("김찬영")
profile("이성우", 33)
profile("강민숙", 40, "java")


'''
김찬영 은 나이가 29이고 주요 언어는 python입니다.
김도규 은 나이가 18이고 주요 언어는 python입니다.
김찬영 은 나이가 18이고 주요 언어는 python입니다.
이성우 은 나이가 33이고 주요 언어는 python입니다.
강민숙 은 나이가 40이고 주요 언어는 java입니다.
'''
#키워드 인자
#profile("강민숙",, "java")
#위 문장은 안된다. 두번째 인자만 기본값이 정해져있으면 어떻게 해야할까?


#다음과 같이 키워드인자를 사용하여 출력할수있다.
profile(name="강민숙", main_language="java")
#강민숙 은 나이가 18이고 주요 언어는 java입니다.

#뒤죽박죽도 가능하다.
profile(main_language="c", name="이경돈")
#이경돈 은 나이가 18이고 주요 언어는 c입니다.

#가변인자
# 만약 인자가 항상 다른 수일 경우면 어떻게 해야할까?
# 예를 들면 A는 사용가능한 언어가 2개고 B가 사용가능한 언어가 5개이다.

# 기본구조
'''
def 함수이름(전달값1, 전달값2, ..., *가변인자):
    실행 명령문1
    실행 명령문2
    ....
    return 반환값
'''

def profile(name, age, *language): # *language는 튜플로 반환된다.
    print("이름은 {0}이고 나이는 {1}살이며, 사용가능한 언어는".format("name", age), end=" ")
    #end=" " 이 구문이 없으면 자동으로 줄바꿈이 된다. 하지만 구문을 넣음으로써 줄바꿈대신 스페이스로 대체된다.
    for lang in language: #language는 튜플형식이다.
        print("{0}".format(lang), end=" ") # =print(lang,end=" ")
    print("입니다. ")

profile("김찬영", 18, "Python", "Java", "C")
#이름은 name이고 나이는 18살이며, 사용가능한 언어는 Python Java C 입니다.
#profile(name="김찬영",age= 18, *langauge=("Python", "Java", "C"))
# 위문장은 오류가 생긴다. 키워드 문자로는 답이 없을까?


#전역변수
#기본구조

#global

#10개의 총기 중 2개의 총기를 경계근무에 쓸 경우
#전역변수를 쓰는 경우
gun=10
def check_gun(use_gun):
    # gun -= use_gun # 전체 총 = 전체 총 - 사용한 총
    # 위와 같은 경우 오류가 뜬다. 함수 외부에 있는 변수를 사용할땐 global키워드를 사용한다.
    global gun #전역변수
    gun -= use_gun
    print("[함수 내] 남은 총 : {0}" .format(gun))

print("전체 총 : {0}" .format(gun))
check_gun(2) # 총2개사용
print("남은 총 : {0}" .format(gun))
'''
전체 총 : 10
[함수 내] 남은 총 : 8
남은 총 : 8
'''

#지역변수를 쓰는 경우
#전달값과 반환값을 적절히 활용하는 방법

gun=10
def check_gun(gun,use_gun):
    gun -= use_gun
    print("[함수 내] 남은 총 : {0}" .format(gun))
    return gun # 남은 총 반환

print("전체 총 : {0}" .format(gun))
gun = check_gun(gun, 2) #현재 총갯수, 사용한 총 매개변수로 사용
rint("남은 총 : {0}" .format(gun))

'''
전체 총 : 10
[함수 내] 남은 총 : 8
남은 총 : 8
'''


