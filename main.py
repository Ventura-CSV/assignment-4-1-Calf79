def main():
    result = []
    # We start our code by using a while command to create a scenario for the code.
    while True:
        start = input('Enter the starting letter: ')
        end = input('Enter the starting letter: ')
       # We use ouur first if command to limit the input to be only one character
        if len(start) != 1 or len(end) !=1:
            print(" Please enter one letter for the start and the end")
            continue
       # We then use our second if command to let the program know we are only accepting aplhabetical characters
        if not (start.isalpha) and (end.isalpha):
            print('Please enter a alphabetic letter for start and end')
            continue
        #Another if command is used to let the program know that the start input should be less than the end input in the alphabet
        if start>end:
            print('Start letter should be less than the end letter')
            continue
        current= start
        #were about to get to the end of the code where we use another while command to tell the program what to do if the start is less than the end, and for it what to print.
        while current<= end:
            result.append(current)
            current = chr(ord(current)+1)
        print(''.join(result))
        break
    """
    ########################################
    Code Your Program here
    ########################################
    """

    print(*result)

    ########################################
    # Do not delete the return statement
    ########################################
    return result


if __name__ == '__main__':
    main()
