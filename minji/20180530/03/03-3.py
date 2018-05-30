for i in range(1, 101):
    print(i),;
    print(" "),;
print("/n");



sum = 0;
for i in range(1, 1001):
    if i%5==0:
        sum += i;
print(sum);



sum = 0;
A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100];
for num in A:
    sum += num;
avg = sum/len(A);
print(avg);



A = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB'];
B = {'A':0, 'B':0, 'AB':0, 'O':0};

for i in A:
    B[i] += 1;

print(B);




numbers = [1, 2, 3, 4, 5]

result = [n*2 for n in numbers if n%2 == 1];
print(result);




A='Life is too short, you need python';
B='aeiou';
result = [a for a in A if a not in B];

print("".join(result));
