name=input()
age=int(input())
numberoftickets=int(input())
price=0
total=0
print(f"Customer name: {name}")
if age <12:
    price=numberoftickets*120
    print("Ticket Price: 120")
elif 12<=age<=59:
    price=numberoftickets*200
    print("Ticket Price: 200")
else:
    price=numberoftickets*150
    print("Ticket Price: 150")
print(f"Number of Tickets: {numberoftickets}")
print(f"Total Before Discount: {price}")
if numberoftickets>=5:
    total=price-price*0.10
    print("Discount: 10%")
    print(f"Final Amount: {total}")
else:
    print("Discount: 0%")
    print(f"Final Amount: {price}")
