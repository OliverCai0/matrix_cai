from display import *
from draw import *
from matrix import *

screen = new_screen()
white = [ 255, 255, 255 ]
yellow = [255,255,0]
red = [255,0,0]
brown = [102,51,0]
black = [0,0,0]

matrix = new_matrix()
add_edge(matrix,0,34,1,3,34,1)
add_edge(matrix,8,30,1,15,25,1)
add_edge(matrix,29,25,1,39,31,1)
add_edge(matrix,43,31,1,43,30,1)
add_edge(matrix,34,20,1,32,20,1)
add_edge(matrix,35,16,1,35,11,1)
add_edge(matrix,36,10,1,36,7,1)
add_edge(matrix,37,6,1,37,3,1)
add_edge(matrix,38,3,1,38,0,1)
add_edge(matrix,8,0,1,8,5,1)
add_edge(matrix,6,8,1,6,12,1)
add_edge(matrix,7,13,1,7,17,1)
add_edge(matrix,8,18,1,8,19,1)
add_edge(matrix,10,21,1,6,25,1)
add_point(matrix,0,34,1)

leye = new_matrix()
add_edge(leye,13,18,1,15,18,1)
add_edge(leye,16,17,1,16,14,1)
add_edge(leye,15,13,1,13,13,1)
add_edge(leye,12,14,1,12,17,1)
add_point(leye,13,18,1)


reye = new_matrix()
add_edge(reye,27,18,1,29,18,1)
add_edge(reye,30,17,1,30,14,1)
add_edge(reye,29,13,1,27,13,1)
add_edge(reye,26,14,1,26,17,1)
add_point(reye,27,18)

nose = new_matrix()
add_edge(nose,21,13,1,23,12,1)
add_edge(nose,19,12,1,21,13,1)

mouth = new_matrix()
add_edge(mouth,20,9,1,24,9,1)
add_edge(mouth,24,5,1,21,5,1)
add_edge(mouth,19,7,1,19,8,1)
add_point(mouth,20,9,1)

rcheek = new_matrix()
add_edge(rcheek,7,12,1,9,12,1)
add_edge(rcheek,10,11,1,10,8,1)
add_edge(rcheek,9,7,1,7,7,1)
print('Example Matrix:')
print_matrix(rcheek)
print()
print('Adding edge ' + str([6,8,1,1]) + ' and ' + str([6,11,1,1]))
add_edge(rcheek,6,8,1,6,11,1)
print_matrix(rcheek)
print()
print('Adding point ' + str([7,12,1,1]))
add_point(rcheek,7,12,1)
print_matrix(rcheek)
print()
print('Creating ident matrix for example matrix')
print_matrix(ident(rcheek,1))
print()
print('Demonstrating Matrix Multiplication')
p2 = [[1,2,3,1],[4,5,6,1]]
p1 = [[1,2,3,1],[4,5,6,1],[7,8,9,1],[10,11,12,1]]
print()
print('M1 = ')
print_matrix(p1)
print()
print('M2 = ')
print_matrix(p2)
print()
print('M1 * M2')
print_matrix(matrix_mult(p1,p2))
rcheek = matrix_mult(ident(matrix,10),rcheek)
#print_matrix(rcheek)


lcheek = new_matrix()
add_edge(lcheek,30,11,1,32,11,1)
add_edge(lcheek,33,10,1,33,8,1)
add_edge(lcheek,32,7,1,30,7,1)
add_edge(lcheek,29,8,1,29,10,1)
add_point(lcheek,30,11,1)


complete_matrices = [matrix,leye,reye,nose,mouth,lcheek]

mutiplier = ident(matrix,10)
for index in range(len(complete_matrices)):
    complete_matrices[index] = matrix_mult(mutiplier,complete_matrices[index])

draw_lines(complete_matrices[0],screen,yellow)
draw_lines(complete_matrices[1],screen,brown)
draw_lines(complete_matrices[2],screen,brown)
draw_lines(complete_matrices[3],screen,brown)
draw_lines(complete_matrices[4],screen,brown)
draw_lines(rcheek,screen,red)
draw_lines(complete_matrices[5],screen,red)

display(screen)



