

######### 3-1-1번 #########
#money = 5000
#card = False

#if money>=4000 or card:
#    print("택시 OK")
#else :
#    print("택시 NO")

######### 3-1-2번 #########
#import random

#lucky_list =[1,9,23,46]
#Rand_Num = random.randrange(1,4)
#if lucky_list[Rand_Num]==lucky_list[2]:
#    print("야호")
#    print(lucky_list[2])
#else : 
#    print(lucky_list[Rand_Num])

######### 3-1-3번 #########
#한글 입력 안되는것 무엇 ?
#number = input("Input number:\n")
#int_number=int(number)
#if int_number < 1 :
#    print("자연수 입력")
#elif int_number%2==0:
#    print("짝수")
#elif int_number%2==1:
#    print("홀수")

######### 3-1-4번 #########
#temp="나이:20,키:180"
#temp_split=temp.split(",")
#print(temp_split)
#str_age=temp_split[0].split(":")[1]
#str_height=temp_split[1].split(":")[1]
#print(str_age,str_height)
#int_age=int(str_age)
#int_height=int(str_height)

#if int_age<30 and int_height>=175 : 
#    print("YES")
#else:
#    print("NO")

######### 3-1-5번 #########
# shirt


######### 3-2-1번 #########
#i=1
#sum=0
#while i<=100:
#    sum=sum+i
#    i=i+1
#print(sum)
######### 3-2-2번 #########
#i=1
#sum=0
#while i<=1000:
#    if i%3==0 :
#        sum=sum+i
#    i=i+1
#print(sum)
######### 3-2-3번 #########
#A = [20, 55, 67, 82, 45, 33, 90, 87, 100, 25]

#sum=0
#while A:
#    temp=A.pop()
#    if temp>=50:
#        sum=sum+temp
#        print(temp)

#print(sum)

######### 3-2-4번 #########
#import sys
#i=0
#j=0
#while i<4:
#    while j<=i:
#        sys.stdout.write('*')
#        j+=1
#    sys.stdout.write('\n')
#    i+=1
#    j=0

######### 3-2-5번 #########
#a = 7
#b = 0
#while a:


######### 3-3-1번 #########
#for a in range (1,101):
#    print(a)

######### 3-3-2번 #########
#sum =0
#for a in range (1,1001):
#    if a%5==0 :
#        sum=sum+a
#    else:
#        continue
#print(sum)

######### 3-3-3번 #########
#A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]
#sum =0
#n=len(A)
#for mark in A:
#    sum=sum+mark
#print(sum/n)

######### 3-3-4번 #########

######### 3-3-5번 #########
#numbers = [1, 2, 3, 4, 5]

#result = [num * 2 for num in numbers if num%2==1]
#print(result)

######### 3-3-6번 #########
A="Life is too short, you need python"

result =[mark for mark in A if mark=='a'or mark=='e' or mark=='i'or mark=='o' or mark=='u']

    

######### 4-1번 #########
#def is_odd(a) :
#    if a%2==0:
#        print("짝수 입니다.")
#    else :
#        print("홀수 입니다.")
#    return 

#is_odd(8)


######### 4-2번 #########
#def avr(*arg):
#    result=0
#    for i in arg:
#        result=result+i
#    return result/len(arg)

#print(avr(1,2,3,4,5,500,515))
######### 4-3번 #########
#def gugudan(a):
#    for i in range(2,10):
#        print(a*i,end = "  ")

#Number=int (input("input number 1~9 :: "))
#if Number>=1 and Number <10 : 
#    gugudan(Number)
#else :
#    print("1~9의 자연수가 아님")

######### 4-4번 #########