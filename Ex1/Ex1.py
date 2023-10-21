def evenOddNumber(num):
    if isinstance(num, int):
        if num % 2 == 0:
            return ('Even!')
        else:
            return ('Odd!')
    else:
        return ('Your input is not integer!')
