import numpy
def rotationMatrix(degree):
    theta = numpy.radians(degree)
    c,s=numpy.cos(theta),numpy.sin(theta)
    return numpy.matrix([[c, -s, 0],
                        [s, c, 0],
                        [0, 0, 1]])
matrix=rotationMatrix(30)
print(matrix)
