x = "Awesome"

def myfunction():
    global x 
    x = "fantastic"
    print("Python is "+x)

myfunction()
print("Python is "+x)