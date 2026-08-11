n=input()
f=n[:5]
l=n[len(n)-5:]
c=n[2:8]
se=n[1::2]
r=n[::-1]
fl=n[1:len(n)-1]
print(f"First 5 characters: {f}")
print(f"Last 5 characters: {l}")
print(f"Characters from 2 to 7 index: {c}")
print(f"Every Second Character: {se}")
print(f"Message in Reverse: {r}")
print(f"Message without first and last character: {fl}")
