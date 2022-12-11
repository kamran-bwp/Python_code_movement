total = 0
counter = 1
condition_value = int(input("how many times you want to execute: "))

while counter <= condition_value:
    i = int(input("input the next grade :"))
    total = total + i
    counter = counter + 1

average = total/10
print(f"Class Average = {average}")




