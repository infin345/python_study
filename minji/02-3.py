
# [문제1] 리스트 인덱싱

a = ['Life', 'is', 'too', 'short', 'you', 'need', 'python'];

print(a[4] + ' ' + a[2]);

# [문제2] 리스트 조인

a = ['Life', 'is', 'too', 'short']

print(a[0] + ' ' + a[1]+ ' ' + a[2]+ ' ' + a[3]);

# [문제3] 리스트의 개수

a = [1, 2, 3];

print(a.index(3) + 1);

# [문제4] 리스트의 append와 extend

a = [1, 2, 3];
a.append([4,5]);

print(a);

a = [1, 2, 3];
a.extend([4,5]);

print(a);

# [문제5] 리스트의 더하기와 extend
# 차이점 없음

print(a);

# [문제6] 리스트 삭제

a = [1, 2, 3, 4, 5];

a.remove(2);
a.remove(4);

print(a);

