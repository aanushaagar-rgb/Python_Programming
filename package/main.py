from myarray.array_module import Array

a = Array([5, 2, 9, 1, 7])

a.display()
a.find_sum()
a.find_max()
a.find_min()
a.search(9)
a.sort_array()

M1 = [[1, 2],
      [3, 4]]
M2 = [[5, 6],
      [7, 8]]

print("\n--- Matrix Operations ---")
a.matrix_add(M1, M2)
a.matrix_subtract(M1, M2)
a.matrix_multiply(M1, M2)
a.matrix_transpose(M1)

print("\n--- Dot Product ---")
V1 = [1, 2, 3]
V2 = [4, 5, 6]
a.dot_product(V1, V2)

print("\n--- Cross Product ---")
a.cross_product(V1, V2)

print("\n--- Matrix Range ---")
a.matrix_range(M1)