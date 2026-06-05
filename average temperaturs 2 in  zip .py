print("welcome to average calculater temperatures")\

print("to calculate the 7 days average temperatures Enter them ")

days=("Saturday","Sunday","Monday","Tusday","Wednsday","Thursday","friday")

temps=tuple(float(input(f"{day} Temperature : ")) for day in days)

sorted_temp=sorted(temps)

average_temp=sum(sorted_temp)/len(sorted_temp)

print("Report of temperature of this week : ")

for day,temp in zip(days,temps):
    print(f"\t{day:<10} : \t{temp}")

print(f"The average of temperature of this week is  {average_temp:.2f}")
