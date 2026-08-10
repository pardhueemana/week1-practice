values = [10, 10, 20, 20, 20, 30, 10, 10, 40,40,50,50]
v2=[]
v2.append(values[0])
for i in range(1,len(values)):
    if values[i]==values[i-1]:
        continue
    else:
        v2.append(values[i])
print(f"Original List: {values}")
print(f"Result: {v2}")