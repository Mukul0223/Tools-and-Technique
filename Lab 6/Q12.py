# Write a menu driven program to read, add, subtract, multiply, divide and transpose two matrices.
class Matrix:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []
        
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(0)
            self.matrix.append(row)

    def read(self):
        print("Enter matrix elements:")
        for i in range(self.rows):
            for j in range(self.cols):
                self.matrix[i][j] = int(input())

    def display(self):
        for row in self.matrix:
            print(row)

    def add(self, mat2):
        if self.rows != mat2.rows or self.cols != mat2.cols:
            print("Error: Matrices must be of same size.")
            return

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] + mat2.matrix[i][j]

        return result

    def subtract(self, mat2):
        if self.rows != mat2.rows or self.cols != mat2.cols:
            print("Error: Matrices must be of same size.")
            return

        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] - mat2.matrix[i][j]

        return result

    def multiply(self, mat2):
        if self.cols != mat2.rows:
            print("Error: Number of columns of matrix 1 must be equal to number of rows of matrix 2.")
            return

        result = Matrix(self.rows, mat2.cols)
        for i in range(self.rows):
            for j in range(mat2.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.matrix[i][k] * mat2.matrix[k][j]
                result.matrix[i][j] = sum

        return result

    def divide(self, scalar):
        result = Matrix(self.rows, self.cols)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[i][j] = self.matrix[i][j] / scalar

        return result

    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.matrix[j][i] = self.matrix[i][j]

        return result


matrix=Matrix(3,3)
while True:
        print("\nMenu:")
        print("1. Add matrices")
        print("2. Subtract matrices")
        print("3. Multiply matrices")
        print("4. Divide matrix by scalar")
        print("5. Transpose matrix")
        print("6. Exit")

        choice = int(input("Enter your choice: "))
        if choice == 1:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            mat1 = Matrix(rows, cols)
            mat2 = Matrix(rows, cols)

            print("Enter elements of first matrix:")
            mat1.read()
            print("Enter elements of second matrix:")
            mat2.read()

            print("\nResultant matrix:")
            result = mat1.add(mat2)
            result.display()

        elif choice == 2:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            mat1 = Matrix(rows, cols)
            mat2 = Matrix(rows, cols)
            print("Enter elements of first matrix:")
            mat1.read()
            print("Enter elements of second matrix:")
            mat2.read()

            print("\nResultant matrix:")
            result = mat1.subtract(mat2)
            result.display()

        elif choice == 3:
            rows1 = int(input("Enter number of rows of first matrix: "))
            cols1 = int(input("Enter number of columns of first matrix: "))
            rows2 = int(input("Enter number of rows of second matrix: "))
            cols2 = int(input("Enter number of columns of second matrix: "))

            if cols1 != rows2:
                print("Error: Number of columns of matrix 1 must be equal to number of rows of matrix 2.")
                continue

            mat1 = Matrix(rows1, cols1)
            mat2 = Matrix(rows2, cols2)

            print("Enter elements of first matrix:")
            mat1.read()
            print("Enter elements of second matrix:")
            mat2.read()

            print("\nResultant matrix:")
            result = mat1.multiply(mat2)
            result.display()

        elif choice == 4:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            mat = Matrix(rows, cols)

            print("Enter elements of matrix:")
            mat.read()

            scalar = int(input("Enter scalar value: "))

            print("\nResultant matrix:")
            result = mat.divide(scalar)
            result.display()

        elif choice == 5:
            rows = int(input("Enter number of rows: "))
            cols = int(input("Enter number of columns: "))

            mat = Matrix(rows, cols)

            print("Enter elements of matrix:")
            mat.read()

            print("\nResultant matrix:")
            result = mat.transpose()
            result.display()

        elif choice == 6:
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")
