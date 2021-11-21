def Sumatoria1(A,B,C):
   n=len(A)
   i=0
   e=0
   while i < n:
     d = A[i]*B[i]+C[i]
     e=e+d
     i+=1

   S=e+n*n
   print('El resultado es: '),print(S)


def Sumatoria2(A,B):
   n=0
   n=len(A)//2
   C=[]
   i=0
   while i<n:
     x=A[i+1]**2
     y=B[2*i]*x
     z=y+B[n+i]
     i+=1
     C.append(z)
   print('El resultado es: '),print(C)   
   return C
   

A=[1,1,1]
B=[2,2,2]
C=[3,3,3]
Sumatoria1(A,B,C)

D=[1,2,3,4]
E=[5,6,7,8]
Sumatoria2(D,E)
