class BasicCalculator:
    def sum(self, numlist: list):
        _sum = 0

        for num in numlist:
            _sum += num

        return _sum
             
# need to add `self` parameter first in instance method 
class ComplexCalculator(BasicCalculator):
    def power(self, base, exponent):
        return base ** exponent
    
    def abs(self, number):
        if number>= 0:
            return number
        
        return -number

basic = BasicCalculator()
complex = ComplexCalculator()

print(basic.sum([1, 2, 3]))
print(complex.sum([1, 2, 3]))
print(complex.power(5,2))
print(complex.abs(-5))
