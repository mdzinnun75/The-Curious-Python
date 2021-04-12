class Bank:
    def rate_of_return(self):
        return 0


class GrowingBank(Bank):
    def rate_of_return(self):
        return 10.5


obj = GrowingBank()
print(obj.rate_of_return())

obj1 = Bank()
print(obj1.rate_of_return())



