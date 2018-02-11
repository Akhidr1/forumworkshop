# allowed papers: 100, 50, 10, 5, and rest of request


def atm_output(request):

    first_digit = int(str(request)[0])

    k = 0

    while k < first_digit:

        print ("give 100")

        k = k + 1

    second_digit = int(str(request)[1])

    if second_digit == 5:

        print ("give 50")

    if second_digit > 5:

        k = 0

        print ("give 50")

        remainder = second_digit - 5

        while k < remainder:

            print ("give 10")

            k = k + 1

    if second_digit < 5:

        k = 0

        while k < second_digit:

            print ("give 10")

            k = k + 1

    third_digit = int(str(request)[2])

    if third_digit == 0:
        print ""

    else:

        if third_digit == 5:

            print ("give 5")

        if third_digit > 5:

            k = 0

            print ("give 5")

            remainder = third_digit - 5

            print ( "give " + str(remainder))

        if third_digit < 5:
            print ( "give " + str(remainder))


atm_output(277)
