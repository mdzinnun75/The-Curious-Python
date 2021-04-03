class Emp:
    def __init__(self, eId, eName, sal):
        self.eId = eId
        self.eName = eName
        self.sal = sal

    def __str__(self):
        #  print(self.sal)
        return("EmpId:{} EmpName:{} EmpSal:{}".format(self.eId, self.eName, self.sal))  # Instead of printing the value, the value should be returned
        # print("EmpId:%d EmpName:%s EmpSal:%g" %(self.eId, self.eName, self.sal))


obj = Emp(101, 'smith', 10000)
print(obj)