def enlarge(n):
    """"
    param n is a number
    function will enlarge n
    """
    return n*100

if __name__ == "_main_":
    y = int(input("Please choose a number:"))
    print(y, enlarge(y))