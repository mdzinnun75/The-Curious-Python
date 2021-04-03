class Emp:
    def __init__(self, eId, eName, sal):
        self.eId = eId
        self.eName = eName
        self.sal = sal

    def display(self):
        #  print(self.sal)
        print("EmpId:{} EmpName:{} EmpSal:{}".format(self.eId, self.eName, self.sal))
        print("EmpId:%d EmpName:%s EmpSal:%g" %(self.eId, self.eName, self.sal))


obj = Emp(101, 'smith', 10000)
obj.display()