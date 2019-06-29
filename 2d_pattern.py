# Find 2D pattern of given 
parent_grid = [[1,2,3,],[4,5,6],[7,8,9]]
def search_in_grid(array):
    for sub_list in array:
        if sub_list in parent_grid:
            print("Found")


if __name__ == "__main__":
    n = int(input("Enter number of rows: "))
    matrix = []
    for i in range(n):
        m = input("Enter elements to be found for row: ").split()
        matrix.append(m)
    search_in_grid(matrix)