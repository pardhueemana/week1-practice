expenses = [250, 1200, 450, 800, 150, 2000, 350]
t=sum(expenses)
avg=t/len(expenses)
h=max(expenses)
l=min(expenses)
print(f"total Expences: {t}")
print(f"Average Expences: {avg}")
print(f"Highest Expence: {h}")
print(f"Lowest Expence: {l}")
print("Expenses greater than 500:")
for i in expenses:
    if i>500:
        print(i)
print("Expenses less than or equal to 500:")
for i in expenses:
    if i<=500:
        print(i)
print("Expences greaterthan Average Expences:")
for i in expenses:
    if i>avg:
        print(i)
