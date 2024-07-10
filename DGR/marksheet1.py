m1=int(input("enter mark1:"))
m2=int(input("enter mark2:"))
m3=int(input("enter mark3:"))
total= m1+m2+m3
if m1>=28 and m2>=28 and m3>28:
    result ="pass"
    per=total/2.1
    if per>=80:
        grade ="A"
    elif per>70:
        grade="B"
    elif per>60:
      grade="C"
    elif per>50:
        grade="D"
    elif per>30:
        grade="E"
else:
        result="Fail"
        per="*"
        grade="F"
print (total,result,per,grade) 
         
    
       

