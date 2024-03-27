#4번
score=int(input("점수를 입력하세요:"))
if score>=90:
    print("장학생", end='')
elif score>=60:
    print("합격", end='')
else:
    print("불합격", end='')
print("입니다.^^")

#5번 (정답:3번)
num=5
res= '짝수'if num%2==0 else'홀수'
print(res)

#6번
nn=[100,200,300,400,500]
nn[1]=777
print(nn)

nn[1]=[444,555]
print(nn)

nn[1:4]=[444,555]
print(nn)

nn[2:]=[]
print(nn)

#9번
hap=0
for n in range(3333,10000):
    if n%1234==0:
        hap+=n
    if hap<=100000:continue
    else:break
    
print(hap)

#8번
hap=0
for n in range(1234, 4568):
    if n%444==0:
        hap+=n
print(hap)

hap=0
n=1234
while n<4568:
    if n%444==0:
        hap+=n
    n+=1
print(hap)

#14번
myData=[[n*m for n in range(1,3)]for m in range(2,4)]
print(myData)

#5번
nn=[100,200,300,400,500]
print(nn[4], nn[-1], nn[-2], nn[1:4], nn[0:1], nn[2:-1], nn[0::2], nn[::-1], nn[::-2], sep='\n')
