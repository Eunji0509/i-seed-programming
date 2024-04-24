#연습문제 2번

#value => self. value
#speed => self.speed


#연습문제 4번

class Horse :
    speed = 0

    def __init__ (self) :
        self.speend = 50


#연습문제 6번 (답:3번)

class Car:
    def method(self):
        print("슈퍼 클래스")

class Sedan(Car):
    def method(self):
        print("서브 클래스")

myCar=Car()
mySedan=Sedan()
myCar.method()
mySedan.method()
        

#연습문제 7번

class Car:
    speed=0

    def upSpeed(self, value):
        self.speed=self.speed+value

class RVCar(Car):
    seatNum=0

    def __init__(self, value):
        self.seatNum=value

    def getSeatNum(self):
        return self.seatNum
