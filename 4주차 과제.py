#1-5
ss = 'Python'
for i in range(0, len(ss)):
    print(ss[i] + '$', end='')

#1-11
inStr=input("문자열 -> ")
outStr=""
for letter in inStr:
    if letter.isalpha(): 
        outStr += letter
print("한글/영문자만 남김 -> " + outStr)    
    
#1-9
inStr, outStr = "Python", ""
strLen = len(inStr)
for i in range(0, strLen) :
    outStr += inStr[strLen-(i+1)]
print("내용을 거꾸로 출력 -- > %s" % outStr)

#2-3
def plus(v1, v2, v3):
    result = 0
    result = v1 + v2 + v3
    return result

hap = plus(100, 200, 300)
print(hap)

#2-4
def f1() :
    print(var) 

def f2() :
    var = 10 
    print(var)

var = 100
f1()
f2()
#  답: 100, 10

#2-11
def addNumber(num):
    if num <= 1:  
        return num
    else:  
        return num + addNumber(num - 1)

print(addNumber(100))

#2-8
def myFunc(p1=1, p2=2, p3=3):
    ret = p1 + p2 + p3
    return ret

print("매개변수 없이 호출 == >", myFunc())
print("매개변수가 1개로 호출 == >" , myFunc(1))
print("매개변수가 2개로 호출 == >", myFunc(1, 2))
print("매개변수가 3개로 호출 == >", myFunc(1, 2, 3))
