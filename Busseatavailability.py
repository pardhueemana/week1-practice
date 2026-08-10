seats = [
    "Available",
    "Booked",
    "Available",
    "Available",
    "Booked",
    "Available",
    "Booked",
    "Available"
]
n=int(input())
t=len(seats)
a=0
b=0
if seats[n-1]=="Booked":
    print("Seat Already Booked")
else:
    seats[n-1]=="Available"
    seats[n-1]="Booked"
    print(f"Seat {n} is booked Sucessfully")
for i in seats:
    if i =="Available":
        a+=1
    else:
        b+=1
print(f"Total Seates: {t}")
print(f"Booked seats: {b}")
print(f"Available seats: {a}")
