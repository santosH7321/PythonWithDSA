def studentInfo(**kwargs):
    for x,y in kwargs.items():
        print(x,"is ",y)
studentInfo(name="Santosh", age=21, city= "Bihar")
studentInfo(name="Nishant", age=25, city=" Bangol")