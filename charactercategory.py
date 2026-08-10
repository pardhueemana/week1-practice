a=input()
u=0
l=0
s=0
d=0
o=0
for i in a:
    if i.isupper():
        u+=1
    elif i.islower():
        l+=1
    elif i.isdigit():
        d+=1
    elif i==' ':
        s+=1
    else:
        o+=1
print(f"Uppercase Letters: {u}")
print(f"Lowercase Letters: {l}")
print(f"Digits: {d}")
print(f"Spaces: {s}")
print(f"Other Characters: {o}")