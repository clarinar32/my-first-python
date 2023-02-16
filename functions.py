def emobilis():
    print("This is my first function")
emobilis()
def calculatesquare():
    x=5
    y= 6
    print(x*y)
calculatesquare()

def majina(fname,lname,age ):
    print(fname+lname+age)
majina("claris" ,"mukhwana", "17")

def schools(schoolname,location,category):
    print(schoolname+location+category)
schools("bunyore girls high school" , "vihiga county" , "national")

# returns the maximum value

def maximum(a,b,c,d,e):
    return max(a,b,c,d,e)
result=maximum(5,15,67,9,89)
print(result)

# returns the minimum value

def minimum(u,v,w,x,y):   
   return min(u,v,w,x,y)
result=minimum(34,56,78,90,76)
print(result)

def print_numbers(nambari):
    for i in range(nambari):
        print(i)
print(10)