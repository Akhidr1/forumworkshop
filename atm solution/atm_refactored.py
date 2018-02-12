# allowed papers: 100, 50, 10, 5, and rest of request

def withdraw(balance, request):

    print ("Current Balance= " + str(balance))
    current_request = request

    if   current_request > balance:
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

        return balance - request


balance = 500

balance = withdraw(balance, 277)
balance = withdraw(balance, 30)
balance = withdraw(balance, 5)
balance = withdraw(balance, 500)
