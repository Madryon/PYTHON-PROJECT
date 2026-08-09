class vector:
    def __init__(self,i,j,k):
        self.i=i
        self.j=j
        self.k=k

    def __str__(self):
        return f"({self.i}i + {self.j}j + {self.k}k)"
    def __add__(self,x):
        return vector(self.i + x.i, self.j+x.j, self.k+x.k)

vector_list=[]

n= int(input("Enter the number of vectors: "))
for _ in range(n):
    i= int(input("Enter the value of i :"))
    j= int(input("Enter the value of j :"))
    k= int(input("Enter the value of k :"))
    vector_list.append(vector(i,j,k))

vector_sum=vector(0,0,0)
for v in vector_list:
    vector_sum=vector_sum + v
    print(v)

print("The sum of the vectors is:", vector_sum)


