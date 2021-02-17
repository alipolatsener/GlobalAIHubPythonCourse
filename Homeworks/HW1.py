import random

matrix, matrix1, matrix2, matrix3=[], [], [], []

#first step creating prime numbers between 1-100
divide=False
for i in range (2,100):
    for j in range(2,i):
        if i%j==0:
            divide=True
            break
    else:
        matrix.append(i)
print(matrix)

#second step: choosing prime numbers randomly and inserting them into 3x3 matrix

for k in range(1,4):                       #choosing three prime number for first matrix
    matrix1.append(random.choice(matrix))  #The choice() method returns a randomly 
                                           #selected element from the specified sequence.
print(matrix1)    
    
for k in range(1,4):                       #choosing three prime number for second matrix
     matrix2.append(random.choice(matrix))
print(matrix2)

for k in range(1,4):                       #choosing three prime number for third matrix
     matrix3.append(random.choice(matrix))           
print(matrix3)
