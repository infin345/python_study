
# [문제1] 문자열 출력 1

print('문제 1 : '+'"점프 투 파이썬" 문제를 풀어보자');

# [문제2] 문자열 출력 2

print('문제 2 : '+'''
Life is too short
You need Python
''');

# [문제3] 공백 추가

A = "%30s" % "PYTHON";

print('문제 3 : '+ A);

# [문제4] 문자열 나누기

A = "881120-1068234";
str1 = A[:6];
str2 = A[7:];

print('문제 4 : ' + str1 + ',' + str2);

# [문제5] 문자열 인덱싱

pin = "881120-1068234";

print('문제 5 : ' + pin[7]);

# [문제6] 문자열 변경

str = "1980M1120";

print('문제 6 : ' + 'M'+str[:4] + str[5:]);

# [문제7] 문자열 포맷

A = "{0:>30}".format("PYTHON");

print('문제 7 : ' + A);

# [문제8] 문자열 찾기

str = "Life is too short, you need python";

a = str.index('short');
print(a);

# [문제9] 문자열 바꾸기 1

str = "a:b:c:d";

print('문제 9 : ' + str.replace(":", "#"));

# [문제10] 문자열 바꾸기 2

str = "a:b:c:d";
str1 = str.split(':');
str2 = str1[0] + str1[1] + str1[2] + str1[3];
str3 = '#'
print('문제 10 : ' + str3.join(str2));
