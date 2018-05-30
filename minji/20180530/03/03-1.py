# [문제1] 조건문1
'''
    홍길동씨는 5,000원의 돈을 가지고 있고 카드는 없다고 한다. 이러한 홍길동씨의 상태는 아래와 같이 표현할 수 있을 것이다.

    >>> money = 5000
    >>> card = False

    홍길동씨는 택시를 타고 목적지까지 가려고 한다. 목적지까지 가기 위해서는 카드를 소유하고 있거나 4,000원의 택시요금이 필요하다고 한다. 홍길동씨는 택시를 탈 수 있는지를 판별할 수 있는 조건식을 작성하고 그 결과를 출력하시오.
'''

money = 5000;
card = False;

if card == True or money >= 4000:
    print("택시 탑승 가능");
else:
    print("택시 탑승 불가능");

# [문제2] 조건문2
'''
    홍길동씨의 행운권 번호는 23번 이라고 한다. 다음은 행운권 당첨번호 리스트이다.

    >>> lucky_list = [1, 9, 23, 46]
    
    홍길동씨가 당첨되었다면 “야호”라는 문자열을 출력하는 프로그램을 작성하시오.
'''

lucky_list = [1, 9, 23, 46]

if lucky_list.count(23):
    print("야호");

# [문제3] 홀수 짝수 판별
'''
    주어진 수가 짝수인지 홀수인지 판별하는 프로그램을 작성하시오.
'''
num = 30;

if num%2 == 0 :
    print("짝수 입니다.");
elif num%2 != 0 :
    print("홀수 입니다.");

# [문제4] 문자열 분석
'''
    다음 문자열을 분석하여 나이가 30미만이고 키가 175이상인 경우에는 YES를 출력하고 아닌 경우에는 NO를 출력하는 프로그램을 작성하시오.

    나이:30,키:180
'''
age = 30;
height = 180;

if age < 30 and height >= 175:
    print("YES");
else:
    print("NO");

# [문제5] 조건문3
'''
    다음 코드의 결과값은 무엇일까?

    >>> a = "Life is too short, you need python"
    >>> if 'wife' in a:
    ...     print('wife')
    ... elif 'python' in a and 'you' not in a:
    ...     print('python')
    ... elif 'shirt' not in a:
    ...     print('shirt')
    ... elif 'need' in a:
    ...     print('need')
    ... else:
    ...     print('none')

'''
a = "Life is too short, you need python";

if 'wife' in a:
    print('wife')
elif 'python' in a and 'you' not in a:
    print('python')
elif 'shirt' not in a:
    print('shirt')
elif 'need' in a:
    print('need')
else:
    print('none')
