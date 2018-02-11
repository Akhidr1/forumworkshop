# allowed papers: 100, 50, 10, 5, and rest of request


def atm_output(request):


    while request - 100 >= 0:

        print ("give 100")

        request = request - 100

    while request - 50 >= 0:

        print ("give 50")

        request = request - 50

    while request - 10 >= 0:

        print ("give 10")

        request = request - 10

    while request - 5 >= 0:

        print ("give 5")

        request = request - 5

    if request > 0:

        print ("give " + str(request))


atm_output(277)
