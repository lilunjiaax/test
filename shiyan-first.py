

'''
name 1.1
judge = 1
while judge !=0 :
    number =  int(input("请输入一个分数(输入数字0推出程序):"))
    judge = number
    if number >= 90:
        print("A")
    if  80 <= number < 90:
        print("B")
    if 60 <= number <80:
        print("C")
    if number <60:
        print("D")
'''

'''
name 1.2
print("请分别输入三个数字：")
a ,b ,c= int(input()),int(input()),int(input())
print(a,b,c)
if a > b:
    a,b = b,a
if b > c:
    b,c = c,b
if a > b:
    a,b = b,a
print("排序后为：")
print(a,b,c)
'''


'''
name 1.3
a = "acesjkdhj"
b = "1326"
print(a+b)
'''


'''
name:1.4
for a in range(1,10):
    for b in range(1,10):
        if a >= b:
            print("%d * %d = %d" % (b,a,a*b) ,end ='      ')
    print(' ')
'''

bingo = 'hello world'
answer=input('请输入正确答案：')
while True:
    if answer==bingo:
        break
    answer=input('抱歉，错了，请重新输入（答案正确才可退出）：')
print('回答正确！')

for i in range(10):
    if i%2 != 0:
        print(i)
        continue
i += 2
print(i)

# continue 结束本次遍历，开始下一次遍历，break 是直接结束循环，跳出循环
'''
# name 1.6
import random
seed = random.randint(1, 10)
a = int(input("请输入您猜的数字："))
while a !=seed:
    if a > seed:
        print("大了")
    if a < seed:
        print("小了")
    a = int(input("请输入您猜的数字："))

print("您猜对了")

'''
