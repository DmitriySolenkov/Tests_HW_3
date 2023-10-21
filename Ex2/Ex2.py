def numberInInterval(num):
    if isinstance(num, int):
        if 25 < num < 100:
            return ('In interval!')
        elif num <= 25:
            return ('Less!')
        else:
            return ('Greater!')
    else:
        return ('Your input is not integer!')
