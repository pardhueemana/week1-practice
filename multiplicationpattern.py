n=int(input())
e=0
o=0
for i in range(1,10+1):
    if (n*i)%2==0:
        e+=1
    else:
        o+=1
print(f"Even Result: {e}")
print(f"Odd Result: {o}")