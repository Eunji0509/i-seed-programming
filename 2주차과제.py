#연습문제 1
print("100")
print(100)
print(50+50)
print("50+50")

#연습문제2
print('%d / %d = %d' % ( 5, 10, 5/10 ))

#연습문제3
print("%04d" % 876)
print("%5s"% "CookBook")
print("%1.1f" % 123.45)

#연습문제4
print("{2:d} {0:d} {1:d}".format(111, 222, 333))

#연습문제11
print(int('1011',2))
print(int('1A',16))

#연습문제13
int('1002',2) # 2진수는 0과 1을 사용
int('1008',8) # 8진수는 0~7까지 사용
int('AAFG', 16) #16진수는 0~9와 A~F까지 이용

#연습문제15
num=12345678
hex_num=hex(num)
oct_num=oct(num)
bin_num=bin(num)

print("10진수=>", num)
print("16진수=>", hex_num)
print("8진수=>", oct_num)
print("2진수=>", bin_num)
