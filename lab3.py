def diagonal_below_product(arr):
    product = 1
    n = len(arr)
    
    for i in range(n):
        for j in range(i+1, n):
            product *= arr[i][j]
    
    return product

# Nümunə olaraq, bir matris yaradırıq:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Bu matris üzərində funksiyanı işə salırıq:
result = diagonal_below_product(matrix)
print("Baş dioqonaldan aşağıda yerləşən elementlərin hasil:", result)
