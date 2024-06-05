# Accept the size of the matrices from the user
rows = int(input("Supply the number of rows: "))
columns = int(input("Supply the number of columns: "))

# Accept the first matrix from the user
mx1 = []
for i in range(1, rows+1):
    row = []
    for j in range(1, columns+1):
        row.append(float(input(f"Supply element ({i},{j}) of matrix 1: ")))
    mx1.append(row)

# Accept the second matrix from the user
mx2 = []
for i in range(1, rows+1):
    row = []
    for j in range(1, columns+1):
        row.append(float(input(f"Supply element ({i},{j}) of matrix 2: ")))
    mx2.append(row)

print()
xn = input("Supply Operator [/,-,+,*]: ")
# Sum the matrices
result = []

for i in range(rows):
    row = []
    for j in range(columns):
        if xn == '+':
            row.append(mx1[i][j] + mx2[i][j])
        elif xn == '-':
            row.append(mx1[i][j] - mx2[i][j])
        elif xn == '/':
            row.append(mx1[i][j] / mx2[i][j])
        elif xn == '*':
            row.append(mx1[i][j] * mx2[i][j])
        result.append(row)


# Print the result
print()
print('Matrix 1: ', mx1)
print('Matrix 2: ', mx2)
print()
print("Operator: ", operator)
print()
print("Result:")
for row in result:
    print(row)
