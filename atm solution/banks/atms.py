class ATM():

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name

    def withdraw(self, request):

    result = self.balance

    print ("Current Balance= " + str(self.balance))

    if   request > self.balance:
         print("Can't give you all this money !!")

    elif request < 0:
         print("More than zero plz!")

    else:

        result = self.balance - request

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


    return result


