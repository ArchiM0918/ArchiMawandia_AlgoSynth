numbers = []
count = 0
while count < 5:
    num = int(input(f"Enter number {count + 1}: "))
    numbers.append(num)
    count = count + 1
    if numbers[count-1] % 2 == 0:
        print("Even")
    else:
        print("Odd")
