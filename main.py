

class Value:
    def __init__(self, data, _children=(), _op='', label=''):
        # super().__init__()
        self.data = data
        self._prev = set(_children)
        self._op = _op
        self.label = label


    def __repr__(self):
        return f"Value(data={self.data})"


    def __add__(self, other ):
        out = Value(self.data + other.data, (self, other), _op='+')
        return out

    def __mul__(self, other ):
        out = Value(self.data * other.data, (self, other), _op='*')
        return out


a = Value(2.0, label='a')
b = Value(-3.0, label='b')
c = Value(10.0, label='c')
e = a * b; e.label = 'e'
d =e + c ; d.label = 'd'
f = Value(-2.0, label='f')
L = d * f; L.label = 'L'

print(d._prev)
print(d._op)

print(a.__repr__())
print(a + b)
print(a * b + c)
# This is the same as (a.__mul__(b)).__add__(c)