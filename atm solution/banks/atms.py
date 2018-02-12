class ATM():

    def __init__(self, balance, bank_name):
        self.balance = balance
        self.bank_name = bank_name


    def withdraw(self, request):

        print ("Welcome to " + self.bank_name)
        print ("Current Balance = " + str(self.balance))

        current_request = request

        if   current_request > self.balance:
             print("Can't give you all this money !!")

        elif current_request < 0:
             print("More than zero plz!")

        else:

            while current_request - 100 >= 0:
                print ("give 100")
                current_request = current_request - 100

            while current_request - 50 >= 0:
                print ("give 50")
                current_request = current_request - 50

            while current_request - 10 >= 0:
                print ("give 10")
                current_request = current_request - 10

            while current_request - 5 >= 0:
                print ("give 5")
                current_request = current_request - 5

            if current_request > 0:
                print ("give " + str(current_request))

            return self.balance - request



