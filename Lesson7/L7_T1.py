class Matrix:

    def __init__(self, list):
        self.list = list

    # def __str__(self):
    #     for row in self.list:
    #         for elem in row:
    #             print(elem, end=' ')
    #         print()
    #     return " "

    def __str__(self):
        # matr_str = ""
        # for row in self.list:
        #     for elem in row:
        #         matr_str += (str(elem) + " ")
        #     matr_str += ("\n")
        # return matr_str
        return "\n" + "\n".join("\t".join(map(str, line)) for line in self.list)

    def __add__(self, other):
        if self.is_same_matrix(other):
            new_mat = self.list
            for i in range(len(self.list)):
                for j in range(len(self.list)):
                    new_mat[i][j] = (self.list[i][j] + other.list[i][j])
            return Matrix(new_mat)
        else:
            return "Матрицы не идентичны"

    def is_same_matrix(self, other):
        if len(self.list) == len(other.list):
            for i in range(len(self.list)):
                print("")
                if len(self.list[i]) != len(other.list[i]):
                    return False
        else:
            return False
        return True


mat1 = Matrix([[31, 32],
               [37, 43]])

mat2 = Matrix([[2, 22],
               [31, 7]])

mat3 = Matrix([[3, 5, 32],
               [2, 4, 6],
               [-1, 64, -8]])

mat4 = Matrix([[3, 5, 8, 3],
               [8, 3, 7, 1]])

print(mat1)
print(mat2)
print(mat3)
print(mat4)

print(f"Сумма матриц: \n{mat1 + mat2}")
print(f"Сумма матриц: \n{mat1 + mat3}")
