def fizzbuzz(n: int) -> None:
    """
    This function prints the numbers from 1 to n, but for multiples of 3, it prints "Fizz"
    and for multiples of 5, it prints "Buzz". For numbers which are multiples of both 3 and 5,
    it prints "FizzBuzz".
    
    :param int n: The number up to which to print the numbers
    
    :return: None
    """
    for i in range(1, n+1):
        strToPrint = ""
        if i % 3 == 0:
            strToPrint += "Fizz"
        if i % 5 == 0:
            strToPrint += "Buzz"
        print(i if strToPrint == "" else strToPrint)

if __name__ == "__main__":
    fizzbuzz(111)
    