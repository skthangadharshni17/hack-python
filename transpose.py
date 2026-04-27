
def get_matrix():
   rows=int(input("Enter the no.of rows:"))
   cols=int(input("Enter the no.of columns:"))
   print("Enter the matrix elements row_wise:")
   matrix=[[int(input())for cols in range(cols)]for rows in range(rows)]
   return matrix
def transpose_matrix(matrix):
   return[[row[i]for row in matrix]for i in range(len(matrix[0]))]
matrix=get_matrix()
result=transpose_matrix(matrix)
print("Transposed matrix:")
for row in result:
   print(row)