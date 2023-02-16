# if statement
x=5
marks=550
grade=70
animals="warthog"
if (x>0):
    print("The number is positive")
# if else statement
if(marks>=550):
    print("You have passed the exam")
else:
   print("you have failed")
# if ....elseif...statement
if(grade<=29 and grade>=0):
    print("you failed")
elif(grade>=30 and grade<=49):
       print("you have passed")
elif(grade>=50 and grade<=79):
    print("you have a credit")
elif(grade>=80 and grade<=100):
    print("you have a distinction")
else:
   print("wrong grade entered")
if(animals=="cows"):
   print("domestic animal")
elif(animals=="hyena"):
    print("wild animal")
elif(animals=="goat"):
    print("it gives us milk")
elif(animals=="donkey"):
   print("it is a beast of burden")
else:
  print("Are you sure that's an animal")
