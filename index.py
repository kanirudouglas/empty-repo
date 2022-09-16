class person():
  def __init__(self,fname,lname):
    self.fname=fname;
    self.lname=lname;
  def printInfo(self):
    print("Your name is {} {} ".format(self.fname,self.lname))
obj1=person("Dennis","Muoki")
obj1.printInfo()
