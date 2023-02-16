try:
    print(myname)
except NameError:
   print("myname is not defined")
except:
    print("Another issue")