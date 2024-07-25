def pascal_triangle(row_num):
    pascal_triangle=[]

    for row in range(row_num):
        currunt_row = [1]*(row+1)
        print(currunt_row)
        for j in range(1,row):
            currunt_row[j] = pascal_triangle[row-1][j-1]+pascal_triangle[row-1][j]
        pascal_triangle.append(currunt_row)
    return pascal_triangle

