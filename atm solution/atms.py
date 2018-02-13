class ATM():

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):

        result = self.balance

        print ("Welcome to " + self.bank_name)
        print ("Current Balance= " + str(result))


        print ("==================================")

        if   request > self.balance:
             print("Can't give you all this money !!")
             print ("==================================")


        elif request < 0:
             print("More than zero plz!")
             print ("==================================")


        else:

            result = self.balance - request

            print ("=>>>>>>>>" +str(result))

            while request > 0:

                if request >= 100:
                    request = request - 100
                    print ("give 100")

                elif request >= 50:
                    request = request - 50
                    print ("give 50")

                elif request >= 10:
                    request = request - 10
                    print ("give 10")

                elif request >= 5:
                    request = request - 5
                    print ("give 5")

                elif request < 5:
                    print("give " + str(request))
                    request = 0
            print ("=>>>>>>>>" +str(result))
            print ("==================================")



            return result



balance1 = 500
balance2 = 1000

atm1 = ATM(balance1," Smart Bank")
atm2 = ATM(balance2," Baraka Bank")

balance1 = atm1.withdraw(277)
balance1 = atm1.withdraw(800)

balance2 = atm2.withdraw(100)
balance2 = atm2.withdraw(2000)
