#Nesibe Özer
x = [2,4,1,6,4,0,0]

def move_zeros_to_left(A):
  if len(A) < 1:
    return

  lengthA = len(A)
  write_index = lengthA - 1
  read_index = lengthA - 1

  while(read_index >= 0):
    if A[read_index] != 0:
      A[write_index] = A[read_index]
      write_index -= 1

    read_index -= 1

  while(write_index >= 0):
    A[write_index]=0;
    write_index-=1
    

move_zeros_to_left(x)
print("After Moving Zeroes to Left: ", x)


x = [ 2,4,1,6,4,0,0]
size = x.__len__(  )
for i in range (0, size):
      for j in range ( 1, size):
            if x[j-1] > x [j]:
                z = x  [j-1]
                x [j-1] = x [j]
                x[j] = z
print ("Numbers in Order:", x )