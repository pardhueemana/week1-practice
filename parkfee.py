n=int(input("Enter the parking hours:"))
s=0
fee=0
total=0
if n<=2:
    fee=n*30
elif 3<=n<=5:
    fee=n*25
else:
    fee=n*20
if fee>150:
    s=20
    total=fee+s
else:
    total=fee
print(f"Parking charges: {fee}")
print(f"Service Charge: {s}")
print(f"Total Amount:{total}")
