import unittest
from fibo import Fibonacci

class Test_Fibonacci(unittest.TestCase):

    def setUp(self):
        self.fibo = Fibonacci()
    
    def get_fib_sequence(self, n):
        return self.fibo.fib_sequence(n)
    
    def test_fibo_8(self):
        self.assertEqual(self.get_fib_sequence(8),21)
    
    def test_fibo_20(self):
        self.assertEqual(self.get_fib_sequence(20), 6765)

    def test_fibo_100(self):
        self.assertEqual(self.get_fib_sequence(100), 354224848179261915075) 

    def test_fibo_541(self):
        self.assertEqual(self.get_fib_sequence(541), 51621232927393794428283281722302417684416215565352081372219649050894399902811978842493025898332777796978839725641)

    def test_fib_2749(self):
        self.assertEqual(self.get_fib_sequence(2749), 14372689553387917661829645671564334144347634506448917723663290089702222530009397342095721197748390703442578832440606734797476053095767644629443572915711792647722348302386453121454440843797863921561581124399573134833792671117667661197245544556688422949193607193895988306702702760603047336208386100938317422813175407356709232675779685357629997245797294804250463809150187026942349354902182628605422407739419382801150894021953277500195893045355811369520046888338772777218694864406890501694863448727599353830662539700881454734823358742184362414868465995609763288002569665002250249)

    def test_fibo_541_is_pandigital_last(self):
        fibn = str(self.get_fib_sequence(541))
        self.assertTrue(self.fibo.is_pandigital(fibn[-9:]))
    
    def test_fibo_541_isnt_pandigital_first(self):
        fibn = str(self.get_fib_sequence(541))
        self.assertFalse(self.fibo.is_pandigital(fibn[:9]))
    
    def test_fibo_100_isnt_pandigital_first(self):
        fibn = str(self.get_fib_sequence(100))
        self.assertFalse(self.fibo.is_pandigital(fibn[:9]))
    
    def test_fibo_100_isnt_pandigital_last(self):
        fibn = str(self.get_fib_sequence(100))
        self.assertFalse(self.fibo.is_pandigital(fibn[-9:]))
    
    def test_fibo_2749_is_pandigital_first(self):
        fibn = str(self.get_fib_sequence(2749))
        self.assertTrue(self.fibo.is_pandigital(fibn[:9]))
    
    def test_fibo_2749_isnt_pandigital_last(self):
        fibn = str(self.get_fib_sequence(2749))
        self.assertFalse(self.fibo.is_pandigital(fibn[-9:]))
