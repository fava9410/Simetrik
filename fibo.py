

class Fibonacci():

    def fib_sequence(self, n: int):
        'Returns Fibonacci sequence for n number'
        a,b = 1,1
        while n > 2 :
            a,b,n = b, b+a, n-1
        return b
    
    def is_pandigital(self, number: str):
        'Checks if a string number has 1-9 digits'

        status = False

        if '1' in number and \
            '2' in number and \
            '3' in number and \
            '4' in number and \
            '5' in number and \
            '6' in number and \
            '7' in number and \
            '8' in number and \
            '9' in number:

            status = True
        
        return status

    def look_for_pandigital_first_last(self, k=0):

        batch = 20000
        limit = k+batch

        while(k < limit):
            fibk = str(self.fib_sequence(k))

            if self.is_pandigital(fibk[:9]) and self.is_pandigital(fibk[-9:]):
                return k
            
            print(k)
            k += 1


def main():

    fibo = Fibonacci()
    fibo.look_for_pandigital_first_last()

if __name__ == "__main__":
    main()