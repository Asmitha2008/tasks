n=int(input("Enter the number of terms for series"))
sequence = [0, 1, 1]
total_sum = 0
print("Sequence:")
for i in range(n):
    if i < 3:
        current_term = sequence[i]
    else:
        current_term = sequence[-1] * 2
        sequence.append(current_term)
    print(current_term, end=" ")
    total_sum += current_term
print(f"\nSum: {total_sum}")