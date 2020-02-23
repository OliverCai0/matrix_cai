"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    x = ''
    y = ''
    z = ''
    one = ''
    for column in matrix:
        x += str(column[0]) + ' '
        y += str(column[1]) + ' '
        z += str(column[2]) + ' '
        one += str(column[3]) + ' '  
        
    print(x)
    print(y)
    print(z)
    print(one)
      

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix,multiplier=1):
    m = int(1 * multiplier)
    identity_matrix = [[m,0,0,0],[0,m,0,0],[0,0,m,0],[0,0,0,m]]
    return identity_matrix


    resultant_matrix = []
    for index in range(len(matrix)):
        resultant_matrix.append(list(range(len(matrix))))
        
    id_matrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    for row_index in range(len(id_matrix)):
        for col_index in range(len(matrix)):
            summation = 0
            for index in range(len(id_matrix[row_index])):
                summation += id_matrix[row_index][index] * matrix[col_index][index]
                resultant_matrix[col_index][row_index] = summation

        
    #print_matrix(resultant_matrix)
    return resultant_matrix


#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
def matrix_mult( m1,m2 ):
    
    x = []
    y = []
    z = []
    one = []
    for column in m1:
        x.append(column[0])
        y.append(column[1])
        z.append(column[2])
        one.append(column[3])
        
    m1_temp = [x,y,z,one]
    
    resultant_matrix = []
    for index in range(len(m2)):
        resultant_matrix.append(list(range(len(m2[index]))))
        
   # id_matrix = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    for m1_row_index in range(len(m1_temp)):
        for m2_col_index in range(len(m2)):
            summation = 0
            for index in range(len(m1[m1_row_index])):
                #print('Multiplying ' + str(m1_temp[m1_row_index][index]) + ' and ' + str(m2[m2_col_index][index]))
                summation += m1_temp[m1_row_index][index] * m2[m2_col_index][index]
            resultant_matrix[m2_col_index][m1_row_index] = summation
            
            
            
            #for index in range(len(m1_temp[row_index])):
            #    summation += m1_temp[row_index][index] * m2[col_index][index]
            #    resultant_matrix[col_index][row_index] = summation

        
    #print_matrix(resultant_matrix)
    return resultant_matrix



def new_matrix(rows = 4, cols = 4):
    m = []
    # for c in range( cols ):
    #     m.append( [] )
    #     for r in range( rows ):
    #         m[c].append( 0 )
    return m
