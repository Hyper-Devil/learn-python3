import math

x=(0.24,0.65,0.95,1.24,1.73,2.01,2.23,2.52,2.77,2.99)
sum=0

for i in x:
    res=(math.cos(i))*(math.log(i))
    sum = sum + res

print(sum)
