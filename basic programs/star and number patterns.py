#right triangle....
# rows=5
# for i in range(1,rows+1):
#     print("*" * i)


#inverted star pattern...
# rows=5
# for i in range(rows,0,-1):
#     print("*" * i)


#square pattern.....
# rows=5
# for i in range(1,rows+1):
#     print("*" * rows)


#number pattern.....
# rows=5
# for i in range(1,rows+1):
#     for p in range(1,i+1):
#         print(p,end=" ");
#     print()


#repeated numbers printing....
# rows = 5
# for i in range(1,rows + 1):
#     print(str(i) * i)


#floyd's triangle....
# rows=5
# num=1
# for i in range(1,rows+1):
#     for j in range(i):
#         print(num,end=" ")
#         num+=1;
#     print()
    



#pyramind triangle.....
rows=5
for i in range(1,rows+1):
    print(" " * (rows-i)+ "*" * (2*i-1))