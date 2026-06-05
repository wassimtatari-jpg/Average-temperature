print("Enter 7 days temperatures to calculate the average of them ")

days=tuple(float(input(f"Enter day temperature {i+1} : ")) for i in range (7))

sorted_tem=sorted(days)

average_tem=sum(days)/len(days)

print(f"The temperatures of this week {sorted_tem} :\nThe average of the {average_tem:.2f}")