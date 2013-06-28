#!/usr/bin/env python
# -*- coding: utf-8

# Реализовать класс рациональных дробей и базовые несколько операций с ними. Пример использования таких дробей
#a = Rational(5, 8)
#b = Rational(3, 4)
#c = a + b
#print c

class rational(object):
    def __init__(self, num, demon=1L):
        self.n = long(num)
        self.d = long(demon)
# The __str__() returns a nice string representation for the rational number
    def __str__(self):
        return "%d/%d" % (self.n, self.d)
# Привести дробь к простому виду (eg 6/8 => 3/4)
    def reduce(self):
        g = gcd(self.n, self.d)
        return rational(self.n//g, self.d//g)
    
    def __add__(self, other):
        print "Operation of addition"
        sum = rational(self.n * other.d + other.n * self.d, self.d * other.d)
        result = sum.reduce()
        return result

    def __sub__(self, other):
        print "Operation of subtraction"
        if isinstance (other, (int, long)):
            return self-rational(other)
        elif isinstance(other,(complex,float)):
            return NotImplemented
        diff = rational(self.n*other.d - other.n*self.d, self.d*other.d)
        return diff.reduce()

    def __div__ (self, other):
        print "Operation of division"
        if isinstance (other,(int,long)):
            return rational(other)/self
        return rational(other.n*self.d, self.d*other.d)

    def __mul__(self, other):
        print "Operation of multiplication"
        mul = rational(self.n * other.d * other.n * self.d, self.d * other.d)
        result = mul.reduce()
        return result
