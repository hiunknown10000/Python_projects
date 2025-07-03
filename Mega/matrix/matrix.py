import numpy as np

# function(add)
def add(ro1, co1, i1, ro2, co2, i2):

    row = ro1 # 1st Row
    col = co1 # 1st Column
    item = i1 # 1st Elements
    a=[]
    for _ in range(col):
        ex = []
        for _ in range(row):
            ex.append(item[0])
            item.pop(0)
        a.append(ex)
    # print(a)

    row2 = ro2 # 2nd Row
    col2 = co2 # 2nd Column
    item2 = i2 # 2nd Elements
    b=[] 
    for _ in range(col2):
        ex2 = []
        for _ in range(row2):
            ex2.append(item2[0])
            item2.pop(0)
        b.append(ex2)
    # print(b)

    s = np.array(a)
    n= np.array(b)
    print(f'Your matrices are: \n\n{s}\n  & \n{n}')
    # print(n)

    output= s + n
    print(f'\nThe result is: \n{output}')

# function(subtract)
def sub(ro1, co1, i1, ro2, co2, i2):
     

    row = ro1 # 1st Row
    col = co1 # 1st Column
    item = i1 # 1st Elements
    a=[]
    for _ in range(col):
        ex = []
        for _ in range(row):
            ex.append(item[0])
            item.pop(0)
        a.append(ex)
    # print(a)

    row2 = ro2 # 2nd Row
    col2 = co2 # 2nd Column
    item2 = i2 # 2nd Elements
    b=[] 
    for _ in range(col2):
        ex2 = []
        for _ in range(row2):
            ex2.append(item2[0])
            item2.pop(0)
        b.append(ex2)
    s = np.array(a)
    n= np.array(b)
    print(f'Your matrices are: \n\n{s}\n  & \n {n}')
    # print(n)

    output= s - n
    print(f'\nThe result is: \n{output}')

# function(multiplaction)
def mul(ro1, co1, i1, ro2, co2, i2):


    row = ro1 # 1st Row
    col = co1 # 1st Column
    item = i1 # 1st Elements
    a=[]
    for _ in range(col):
        ex = []
        for _ in range(row):
            ex.append(item[0])
            item.pop(0)
        a.append(ex)
    # print(a)

    row2 = ro2 # 2nd Row
    col2 = co2 # 2nd Column
    item2 = i2 # 2nd Elements
    b=[] 
    for _ in range(col2):
        ex2 = []
        for _ in range(row2):
            ex2.append(item2[0])
            item2.pop(0)
        b.append(ex2)

    s = np.array(a)
    n= np.array(b)
    print(f'Your matrices are: \n\n{s}\n  & \n{n}')
    # print(n)

    output= s @ n
    print(f'\nThe result is: \n{output}')




# Order1 HANDLE
print('Enter your choice :)')
last= int(input("[Addition(1)/Subtraction(2)/Multiplication(3)] : "))
if last>3:
    print("Opps! wrong choice")
    exit()

print('\nTell us the 1st Matrix order\n')
r = int(input('[ row ] : '))
c = int(input('[ column ] : '))

# Input the 1st Matrix elements in a list

elements = input('Enter the all Matrix elments in [x,y,z,a,b,c...] order : ')
# elements= list(elements)
# print(elements)
str_list = elements.split(",")  # Split by comma
elements= [int(num.strip()) for num in str_list]
x= len(elements)
if (r*c) != x:

    # Here i use x as the counter
    print(f'Total number needs {r*c}, but your input {x} numbers, which is not satisfy')
    exit()
else:
    print (f'\nYou entered ---> {elements}')



# Order2 HANDLE
print('Tell us the 2nd Matrix order\n')
r2 = int(input('[ row ] : '))
c2 = int(input('[ column ] : '))

# Input the 2nd Matrix elements in a list

elements2 = input('Enter the all Matrix elments in [x,y,z,a,b,c...] order : ')
# elements2= list(elements2)
# print(elements2)
str_list2=elements2.split(',') # Split by comma
elements2=[int(num2.strip()) for num2 in str_list2]

x2= len(elements2)

if (r2*c2) != x2:

    # Here I used x2 as the counter
    print(f'Total number needs {r2*c2}, but your input {x2} numbers, which is not satisfy')
else:
    print (f'\nYou entered ---> {elements2}')

# At last the output is ( r, c, elements )
# At last the output is ( r2, c2, elements2 )
if last==1:
    add(r, c, elements, r2, c2, elements2)
elif last==2:
    sub(r, c, elements, r2, c2, elements2)
elif last==3:
    mul(r, c, elements, r2, c2, elements2)




# print(a.T) # for a transpose
# print(b)
# print(add)
