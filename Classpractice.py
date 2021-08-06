#Class 실습



###예시1:
class j:
    def __init__(self):
        self.name=input("이름 :")
        self.age=input("나이 :")
    def show(self):
        print('나의 이름은 {}, 나이는 {}입니다'.format(self.name, self.age))

a = j() #a는 객체, a는 j의 인스턴스
a.show() #이름:박은정, 나이: 25 -> 출력: 나의 이름은 박은정, 나이는 25입니다

class j2(j): #클래스 상속
    def __init__(self):
        super().__init__() #super()는 자식 클래스에서 부모 클래스의 메서드를 사용하고 싶을 경우 사용
        self.gender=input('성별 :')
    def show(self):
        print('나의 이름은 {}, 성별은 {}자, 나이는 {}입니다'.format(self.name, self.gender, self.age))

a=j2()
a.show()

class Pokemon:
    pokemon_a = "pikachu"

    def print_pika():
        print("Hello Pika")

print(Pokemon.pokemon_a) #pikachu
Pokemon.print_pika() #Hello Pika



###예시2:
#인스턴스에서도 활용 가능
class Pokemon: #포켓몬이라는 클래스 생성
    #생성자 함수: 클래스가 인스턴스화 될 때 사용되는 함수
    def __init__(self, pokemon_name): #생성자 함수 __init
	    self.name = pokemon_name

    def hello(self):
        return f"I am {self.name}"

pikachu=Pokemon('Pikachu') #인스턴스
eevee=Pokemon('Eevee') #인스턴스

print(pikachu.name) #Pikachu
print(pikachu.hello()) #I am Pikachu
print(eevee.name) #Eevee       
print(eevee.hello()) #I am Eevee



###예시3:
from random import randint
class Product:
    def __init__(self, name, price=30, size=20, warmness=0.5, sweetness=0.5, identifier=randint(1000000,9999999)):
        self.name=name
        self.price=price
        self.size=size
        self.warmness=warmness
        self.sweetness=sweetness
        self.identifier=identifier
        
    def sellability(self):
        sel=self.size/self.price

        if sel < 0.5:
            return "Not so sellable..."
        elif sel >=0.5 and sel < 1.0:
            return "Kinda sellable"
        else:
            return "Very sellable!"

    def calory(self):
        cal=self.size*self.sweetness

        if cal < 10:
            return "...it's light"
        elif cal >= 10 and cal < 50:
            return "It's adequate."
        else:
            return "It's really heavy..!!"

prod=Product('A Cold Drink')
print(prod.price) #30
print(prod.sellability()) #Kinda sellable
print(prod.calory()) #It's adequate.

class Tea(Product): #클래스 상속, 사이즈 변경
    def __init__(self, name, price=30, size=10, warmness=0.5, sweetness=0.5, identifier=randint(1000000,9999999)):
        super().__init__(name, price, size, warmness, sweetness, identifier)  

    def calory(self): #같은 이름의 메소드 사용하면 대체
        return "...it's a tea. Only a few calories"

    def drink(self):
        warm=self.warmness

        if warm < 0.5:
            return "it's too cold..."
        elif warm >= 0.5 and warm < 1.0:
            return "Oh, it's warm!"
        else:
            return "It's too hot!!"

tea = Tea('Green Tea')
print(tea.drink()) #Oh, it's warm!
print(tea.size) #10
print(tea.calory()) #...it's a tea. Only a few calories

