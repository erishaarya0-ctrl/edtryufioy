numbers = [-4, 6, 2, 0, 0, 1, 1]

print("\nPART 1: Slices and Their Sums")
print("Full Array:", numbers)

index = 2
left_slice = numbers[:index]
right_slice = numbers[index + 1:]

print("Left of index", index, ":", left_slice)
print("Right of index", index, ":", right_slice)
print("Left Sum:", sum(left_slice))
print("Right Sum:", sum(right_slice))

print("\nPART 2: Left-Right Balance")

for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])
    print("Index", i, "-> Left Sum:", left_sum, "| Right Sum:", right_sum)

print("\nPART 3: Equilibrium Point")

for i in range(len(numbers)):
    left_sum = sum(numbers[:i])
    right_sum = sum(numbers[i + 1:])
    
    if left_sum == right_sum:
        print("Equilibrium found at index:", i)
        print("Element:", numbers[i])

values =[3, 6, 2, 2, 4, 1]

print("\nPART 4: Subarray Window")
print("Array:", values)

window_sum = 0

for i in range(len(values)):
    window_sum = window_sum + values[i]
    print("Window from index 0 to", i, ":", values[:i + 1], "| Sum:", window_sum)

print("\nPART 5: Target Sum Search")
target = 10

for start in range(len(values)):
    for end in range(start + 1, len(values) + 1):
        sub_array = values[start:end]
        
        if sum(sub_array) == target:
            print("Target found from index", start, "to", end - 1, ":", sub_array)
