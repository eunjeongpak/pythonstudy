#Class

#클래스와 객체
#과자 틀 → 클래스 (class)
#과자 틀에 의해서 만들어진 과자 → 객체 (object)

#객체와 인스턴스의 차이
#class Cookie가 있을 때 a = Cookie() -> a는 객체, a 객체는 Cookie의 인스턴스
#인스턴스라는 말은 특정 객체(a)가 어떤 클래스(Cookie)의 객체인지를 관계 위주로 설명할 때 사용
#"a는 객체"라는 표현이 어울리며 "a는 Cookie의 인스턴스"라는 표현이 훨씬 잘 어울림

###예시: 계산기
class Calculator:
    def __init__(self):
        self.result = 0

    #더하기 기능
    def add(self, num):
        self.result += num
        return self.result

    #빼기 기능
    def sub(self, num):
        self.result -= num
        return self.result

#Calculator 클래스로 만든 별개의 계산기 cal1, cal2
#파이썬에서는 이것을 객체라고 함
#계산기(cal1, cal2)의 결괏값 역시 다른 계산기의 결괏값과 상관없이 독립적인 값을 유지
cal1 = Calculator()
cal2 = Calculator()

print(cal1.add(3)) #3
print(cal1.add(8)) #3+8=11
print(cal1.sub(4)) #11-4=7

print(cal2.add(2)) #2
print(cal2.add(4)) #2+4=6
print(cal2.sub(1)) #6-1=5

###예시: 사칙연산 클래스 만들기
class FourCal:
    #메서드(클래스 안에 구현된 함수)
    #def 함수명(매개변수):
        #수행할 문장 ...
    def __init__(self, first, second): #생성자 -> 객체가 생성될 때 초깃값 설정하기 보다는 생성자 구현
        self.first=first
        self.second=second
    def setdata(self, first, second):
        self.first=first
        self.second=second
    def add(self):
        result=self.first+self.second
        return result
    def mul(self):
        result=self.first*self.second
        return result
    def sub(self):
        result=self.first-self.second
        return result
    def div(self):
        result=self.first/self.second
        return result

# a=FourCal()
# b=FourCal()
#print(type(a)) #<class '__main__.FourCal'> -> 객체 a가 FoulCal의 객체임

#생성자 없는 경우
#a.setdata(4,2)
#b.setdata(3,8)

# print(a.first) #4
# print(a.second) #2

# print(a.add()) #4+2=6
# print(a.sub()) #4-2=2
# print(a.mul()) #4x2=8
# print(a.div()) #4/2=2

# print(b.add()) 
# print(b.sub()) 
# print(b.mul()) 
# print(b.div()) 

#생성자 생성 후 
a=FourCal(4,2)
print(a.first)
print(a.second)
print(a.add())
print(a.div())

#클래스 상속
#어떤 클래스 만들 때 다른 클래스 기능을 물려받을 수 있게 만드는 것
#기존 클래스를 변경하지 않고 기능을 추가하거나 기존 기능을 변경하려고 할 때 사용
###위의 예시 이어서 ,, 
class MoreFourCal(FourCal):
    def pow(self):
        result=self.first**self.second
        return result

a = MoreFourCal(4, 2)
print(a.add())
print(a.mul())
print(a.sub())
print(a.div())
print(a.pow())

#메서드 오버라이딩(Overriding, 덮어쓰기)
#부모 클래스(상속한 클래스)에 있는 메서드를 동일한 이름으로 다시 만드는 것
# a=FourCal(4, 0)
# print(a.div()) #division by zero 오류 뜸
# 오류가 아닌 0을 돌려주고 싶다면, 메서드 오버라이딩 사용
class SafeFourCal(FourCal):
    def div(self):
        if self.second==0:
            return 0
        else:
            return self.first/self.second

a=SafeFourCal(4, 0)
print(a.div()) #0

